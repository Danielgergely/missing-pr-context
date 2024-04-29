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

    def create_combined_plot(self, main_categories: list, sub_categories: list[tuple[str, str]],
                             title: str = "Combined charts"):
        fig = sp.make_subplots(rows=len(main_categories), cols=len(sub_categories), subplot_titles=main_categories)

        for i, main_category in enumerate(main_categories):
            chart_data = self._data[self._data["PR category"] == main_category]
            color_map = {category: color for category, color in zip(sub_categories, px.colors.qualitative.Plotly)}
            for j, sub_category in enumerate(sub_categories):
                if sub_category[1] == "bar":
                    fig.add_trace(self.getBarPlot(data=chart_data[sub_category[0]].value_counts(),
                                                  title=f"{sub_category[0]}",
                                                  color=color_map[sub_category],
                                                  show_legend=False,
                                                  legendgroup=(i + 1)),
                                  row=(i + 1), col=(j + 1))
                elif sub_category[1] == "box":
                    fig.add_trace(self.getBoxPlot(data=chart_data[sub_category[0]].value_counts(),
                                                  title=f"{sub_category[0]}",
                                                  color=color_map[sub_category],
                                                  show_legend=False,
                                                  legendgroup=(i + 1)),
                                  row=(i + 1), col=(j + 1))

        # missing_linkage = self._data[self._data["PR category"] == "Missing linkage"]
        # fig.add_trace(go.Box(y=missing_linkage["Comment count"].value_counts(),
        #                      name="Comment count",
        #                      showlegend=True,
        #                      ),
        #               row=1, col=1)

        fig.update_layout(height=500 * len(main_categories), width=300 * len(sub_categories), title_text=title,
                          legend_tracegroupgap=340)
        fig.update_xaxes(title_text="Categories")
        fig.update_yaxes(title_text="Counts")
        fig.show()

    def getBarPlot(self, data, title, show_legend, color, legendgroup):
        return go.Bar(x=data.index,
                      y=data.values,
                      name=title,
                      showlegend=show_legend,
                      legendgroup=legendgroup,
                      marker_color=color)

    def getBoxPlot(self, data, title, show_legend, color, legendgroup):
        return go.Box(y=data,
                      name=title,
                      showlegend=show_legend,
                      marker_color=color,
                      legendgroup=legendgroup)
