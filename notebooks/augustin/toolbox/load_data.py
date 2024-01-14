import numpy as np

def read_off(path_to_data, figname):
    file = path_to_data + "meshes/" + figname + '.off'
    with open(file) as f:
        if 'OFF' != f.readline().strip():
            raise('Not a valid OFF header')
        try:
            n_verts, n_faces, n_dontknow = tuple([int(s) for s in f.readline().strip().split(' ')])
            verts = [[float(s) for s in f.readline().strip().split(' ')] for i_vert in range(n_verts)]
            faces = [[int(s) for s in f.readline().replace('   ', ' ').strip().split(' ')][1:] for i_face in range(n_faces)]
        except:
            print(f.readline())
        return np.array(verts), np.array(faces)
    
    
def read_npy(path_to_data, figname):
    file = path_to_data + "numpy/" + figname + '.npy'
    return np.load(file)
