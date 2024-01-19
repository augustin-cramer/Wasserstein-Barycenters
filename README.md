# Wasserstein Barycenters

This repository main objective is to implement the Wasserstein barycenters algorithm as it is described in [Solomon et al. (2015), _Convolutionnal Wasserstein Distances: Efficient Optimal Transportation on Geometric Domains_](https://hal.science/hal-01188953).

Install the required libraries by using the following command :

```cmd
pip install -r requirements.txt
```

## Repository content

### Demo notebooks

A demonstration of how we proceed to do the shape interpolation is exposed in the notebook `wasserstein_barycenters_3d.ipynb` that can be found at the root of this repo. Insights about how we dealt with 3D shapes is exposed in `3d_shapes_management.ipynb`. The shapes are rendered using _plotly_ and the plots are heavy so we couldn't upload them on GitHub. The results are displayed in our report, but you can still execute them to play with the 3d barycenters.

### Source code

The source code of all the tools that used during our project can be found in the directory `wasserstein_barycenters/`.

#### 1 - Main script

Inside this directory, the main script `wasserstein_barycenters_3d.py`contains the implementation of the algorithm described in our studied paper.

#### 2 - Utils

Then the directory `utils/` contains several tools that we developped for our work, let's go through some of them.

##### a - Mesh to point cloud

Our first problematic was to design an indicator function of the interior of the shapes that we had, that were originally encoded as closed triangular meshes. Using the [Möller-Trumbore intersection algorithm](https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm), we construct such a fonction on a discrete support from the mesh.

##### b - Gaussian blur kernel

The heat kernel used in the Wassersetein barycenters algorithm uses a heat kernel that is described as a Gaussian convolution. We implement such a convolution for 3d arrays.

##### c - Point cloud to mesh

After having computed the Wasserstein barycenters, we end up with a new point cloud that is the ndicator function of the interior of the barycenter. `point_cloud_to_mesh.py` implements a function that uses a simple neighbor count to figure out which points belong to the surface of the shape and then uses `pyvista` to reconstruct a closed triangular mesh out of it. This allows us to leverage the lighting feature of `plotly` to visualize the barycenters in 3D.

### Data

The `data\` directory is divided in two sub-directories containing meshes and numpy data. Our raw data was only the meshes but we provide numpy files for a faster execution of the demo notebooks.

## Originality of the code

Even tho a pseudo-code algorithm is given in the paper, there were few technical informations for the implementation. The inputs of the algoritm were supposed to be a probability distribution representing the interior of the shape and a heat kernel, as well as some area weights.

We figured out entirely by ourselves how to construct the interior of the shape. But then we struggled to understand what the other inputs of the algorithm should be. We investigated in the paper's [repository](https://github.com/gpeyre/2015-SIGGRAPH-convolutional-ot), where the programs to replicate the images displayed in the paper were implemented in MATLAB. We weren't familiar with this language so we spent a lot of time studying them. There we understood that the heat kernel were supposed to be Gaussian kernel - that was rather unclear in the paper because evoked in different parts than the one explaining shape insterpolation.

Then we made our own python implementation of the Wasserstein algorithm, that follows the structure proposed in the paper. We encountered some computationnal issues that we solved by ourselves.

The rest of the code presented in this repository is original and designed for the purpose of this project.
