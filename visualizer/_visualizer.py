import pandas as pd
import plotly.subplots as sp
import plotly.graph_objs as go
import plotly.express as px


class Visualizer:
    _data: pd.DataFrame

    def __init__(self, data: pd.DataFrame):
        self._data = data

    def create_barplots(self, x_values: list[tuple], sub_titles: list[tuple] | None = None,
                        title: str = "Subplots for each category"):
        if sub_titles is None:
            sub_titles = x_values
        sub_titles = [f"{i + 1}. {x[0]} x {x[1]}" for i, x in enumerate(sub_titles)]
        fig = sp.make_subplots(rows=len(x_values), cols=1, subplot_titles=sub_titles)

        unique_categories = self._data[x_values[0][1]].unique()
        color_map = {category: color for category, color in zip(unique_categories, px.colors.qualitative.Plotly)}

        for i, x in enumerate(x_values, start=1):
            for category in self._data[x[1]].unique():
                data = self._data[self._data[x[1]] == category][x[0]].value_counts()
                fig.add_trace(
                    go.Bar(x=data.index,
                           y=data.values,
                           name=f'{x[1]}: {category}',
                           marker_color=color_map[category],
                           legendgroup=i),
                    row=i, col=1,
                )

        fig.update_layout(height=400 * len(x_values), width=800, title_text=title,
                          legend_tracegroupgap=340)
        fig.update_xaxes(title_text="Categories")
        fig.update_yaxes(title_text="Counts")
        fig.show()

    def create_boxplots(self, x_values: list[tuple], sub_titles: list[tuple] | None = None,
                        title: str = "Subplots for each category"):
        if sub_titles is None:
            sub_titles = x_values
        sub_titles = [f"{i + 1}. {x[0]} x {x[1]}" for i, x in enumerate(sub_titles)]
        fig = sp.make_subplots(rows=len(x_values), cols=1, subplot_titles=sub_titles)

        unique_categories = self._data[x_values[0][1]].unique()
        color_map = {category: color for category, color in zip(unique_categories, px.colors.qualitative.Plotly)}

        for i, x in enumerate(x_values, start=1):
            for category in self._data[x[1]].unique():
                data = self._data[self._data[x[1]] == category][x[0]]
                fig.add_trace(
                    go.Box(y=data.value_counts(),
                           name=f'{x[1]}: {category}',
                           marker_color=color_map[category],
                           showlegend=False,
                           boxpoints=False),
                    row=i, col=1,
                )

        fig.update_layout(height=500 * len(x_values), width=800, title_text=title)
        fig.update_xaxes(title_text="Categories")
        fig.update_yaxes(title_text="Counts")
        fig.show()

    def create_combined_plot(self, main_categories: list, sub_categories: list[tuple[str, str, str]],
                             title: str = "Combined charts", threshold: int = 0.95, dark_mode: bool = True):

        global_maxs = {}

        for main_category in main_categories:
            filtered_data = self._data[self._data["PR category"] == main_category]
            for sub_category in sub_categories:
                if sub_category[1] == "box":
                    t = filtered_data[sub_category[0]].quantile(threshold)
                    filtered_chart_data = filtered_data[filtered_data[sub_category[0]] <= t]
                    global_maxs[sub_category[0]] = round(filtered_chart_data[sub_category[0]].max() * 1.15)

        subplot_titles = [" " for _ in range(len(main_categories) * len(sub_categories))]
        fig = sp.make_subplots(rows=len(main_categories), cols=len(sub_categories), subplot_titles=subplot_titles)

        for i, main_category in enumerate(main_categories):
            chart_data = self._data[self._data["PR category"] == main_category]

            color_map = {category: color for category, color in zip(sub_categories, px.colors.qualitative.Plotly)}
            for j, sub_category in enumerate(sub_categories):
                if sub_category[1] == "bar":
                    fig.add_trace(self.getBarPlot(data=chart_data[sub_category[0]].value_counts(),
                                                  title=f"{sub_category[0]}",
                                                  color=color_map[sub_category],
                                                  show_legend=False),
                                  row=(i + 1), col=(j + 1))
                elif sub_category[1] == "box":
                    t = chart_data[sub_category[0]].quantile(threshold)
                    filtered_chart_data = chart_data[chart_data[sub_category[0]] <= t]
                    fig.add_trace(self.getBoxPlot(data=filtered_chart_data[sub_category[0]],
                                                  title=f"{sub_category[0]}",
                                                  color=color_map[sub_category],
                                                  show_legend=False),
                                  row=(i + 1), col=(j + 1))
                    fig.update_yaxes(range=[0, global_maxs[sub_category[0]]], row=(i + 1),
                                     col=(j + 1))

                fig.update_yaxes(title_text=f"{sub_category[2]}", row=(i + 1), col=(j + 1))

            fig.add_annotation(
                dict(
                    x=0.5,
                    y=1 - (1 / len(main_categories) * i) + 0.05 - (0.05 * i),
                    showarrow=False,
                    text=f"{main_category} - {len(chart_data)} ({len(chart_data) / len(self._data) * 100:.2f}%)",
                    xref="paper",
                    yref="paper",
                    font=dict(size=18, color="white" if dark_mode else "black"),
                )
            )

        fig.update_layout(title_text=f"{title} - {threshold * 100}% threshold",
                          template='plotly_dark' if dark_mode else 'plotly')
        fig.show()

    def getBarPlot(self, data, title, show_legend, color):
        total = data.sum()
        percentages = data / total * 100
        return go.Bar(x=percentages.index,
                      y=percentages.values,
                      name=title,
                      showlegend=show_legend,
                      marker_color=color)

    def getBoxPlot(self, data, title, show_legend, color):
        return go.Box(y=data,
                      name=title,
                      showlegend=show_legend,
                      marker_color=color,
                      boxpoints=False)
