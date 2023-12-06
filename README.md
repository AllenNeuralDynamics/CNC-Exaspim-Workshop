# AIND - UW CNC ExaSPIM Workshop

Data and notebooks for the Hackacollabathon on December 6, 2023

This capsule contains 4 notebooks:
- `create_manifest.ipynb` is the notebook that is run as the `Reproducible Run`. It creates a dataframe of the available reconstructed neurons across both the AIND ExaSPIM and the Mouselight data. It takes ~1.5 minutes to run.
- `networkx.ipynb` demonstrates how to interact with the reconstruction jsons, visualizing morphology, and computing various morphological features. It leverages the python package networkx.
- `Medulla.ipnyb` demonstrates a specific analysis of neurons with soma in the Medulla, clustering them based on their projection patterns.
- `View_Neuron.ipynb` demonstrates 3D visualization tools.

The data in this capsule are publicly available, so if you choose to deploy this capsule locally you can still access the data.
The Mouselight data can be downloaded from the mouselight browser.
The AIND ExaSPIM data are available in our public AWS bucket in the locations below. You will need to adjust the paths in the notebooks as needed:

s3://aind-open-data/exaSPIM_609281_2022-11-03_13-49-18_reconstructions

s3://aind-open-data/exaSPIM_651324_2023-03-06_15-13-25_reconstructions

s3://aind-open-data/exaSPIM_653158_2023-06-01_20-41-38_reconstructions

s3://aind-open-data/exaSPIM_653980_2023-08-10_20-08-29_reconstructions



<h2>Some ideas of things to explore with these data</h2>:

- Can we separate PT and IT cells in the cortex? What are the features that best separate them?
- Compare projection patterns of neurons with soma in VM to those in VA/VL.
- Cluster neurons based on projection patterns to parcellate nuclei in medulla and/or thalamus (see the Medulla notebook). Are dendritic morphological feature different between neurons with soma in the two main compartments of the medulla?
- Can you build a decoder to predict soma location based on morphological features?
- Are there morphological differences between neurons of different cell types? (this might be stymied by sampling issues - might not be enough neurons of different cell types yet)

