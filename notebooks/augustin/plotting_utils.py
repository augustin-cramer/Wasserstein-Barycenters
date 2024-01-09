import plotly.graph_objects as go

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
    
def read_off(file):
    if 'OFF' != file.readline().strip():
        raise('Not a valid OFF header')
    n_verts, n_faces, n_dontknow = tuple([int(s) for s in file.readline().strip().split(' ')])
    verts = [[float(s) for s in file.readline().strip().split(' ')] for i_vert in range(n_verts)]
    faces = [[int(s) for s in file.readline().strip().split(' ')][1:] for i_face in range(n_faces)]
    return verts, faces