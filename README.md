# Convolutionnal-Wasserstein-Distances

This repository main objective is to implement the Wasserstein barycenters algorithm as it is described in [Solomon et al. (2015)_Convolutionnal Wasserstein Distances: Efficient Optimal Transportation on Geometric Domains_](https://hal.science/hal-01188953) by A. Conrad, A. Cramer and N. Farhan.

## Setup your environment

Install the required libraries by using the following command :

```cmd
pip install -r requirements.txt
```

## Demo notebook

A demonstration of how we proceed to do the shape interpolation is exposed in the notebook `wasserstein_barycenters_3d.ipynb` thet can be found at the root of this repo.

## Description of the source code

The source code of all the tools that used during our project can be found in the directory `wasserstein_barycenters`.

### Main script

Inside this directory, the main script `wasserstein_barycenters_3d.py`contains the implementation of the algorithm described in our studied paper.

### Utils

Then the directory utils contains several tools that we developped for our work, let's go through some of them.

#### Mesh to point cloud

Our first problematic was to design an indicator function of the interior of the shapes that we had, that were originally encoded as closed triangular meshes. Using the [Möller-Trumbore intersection algorithm](https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm), we construct such a fonction on a discrete support from the mesh.

#### Gaussian blur kernel

The heat kernel used in the Wassersetein barycenters algorithm uses a heat kernel that is described as a Gaussian convolution. We implement such a convolution for 3d arrays.

#### Point cloud to mesh

After having computed the Wasserstein barycenters, we end up with a new point cloud that is the ndicator function of the interior of the barycenter. This file implements a function that uses a simple neighbor count to figure out which points belong to the surface of the shape and then uses `pyvista` to reconstruct a closed triangular mesh out of it. This allows us to leverage the lighting feature of `plotly` to visualize the barycenters in 3D.
