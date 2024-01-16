import plotly.graph_objects as go
import numpy as np

def plot_mesh(arr_verts, arr_faces, show_axis=True):
    fig = go.Figure(data=[
        go.Mesh3d(
            # 8 vertices of a cube
            x=arr_verts[:,0],
            y=arr_verts[:,1],
            z=arr_verts[:,2],
            # i, j and k give the vertices of triangles
            i = arr_faces[:,0],
            j = arr_faces[:,1],
            k = arr_faces[:,2],
            color='cyan', 
        ),
    ])
    
    if not show_axis:
        fig.update_scenes(xaxis_visible=False, yaxis_visible=False,zaxis_visible=False )

    fig.show()
    
