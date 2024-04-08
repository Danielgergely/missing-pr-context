import pandas as pd
import plotly.subplots as sp
import plotly.graph_objs as go
import plotly.express as px


class Visualizer:
    _data: pd.DataFrame

    def __init__(self, data: pd.DataFrame):
        self._data = data

    def create_subplots(self, x_values: list[tuple], sub_titles: list[tuple] | None = None,
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
        fig.show()
