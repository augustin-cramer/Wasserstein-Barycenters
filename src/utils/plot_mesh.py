import plotly.graph_objects as go


def plot_mesh(vertices, faces, show_axis=True, **kwargs):
    fig = go.Figure(
        data=[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=faces[:, 0],
                j=faces[:, 1],
                k=faces[:, 2],
                **kwargs
            ),
        ]
    )

    if not show_axis:
        fig.update_scenes(
            xaxis_visible=False, yaxis_visible=False, zaxis_visible=False
        )

    fig.show()
