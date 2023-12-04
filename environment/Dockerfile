# hash:sha256:48562c8238f0a13a65e08e1584f50225df890bcd59776e5946e21ccc1a04f403
FROM registry.codeocean.allenneuraldynamics.org/codeocean/mambaforge3:23.1.0-4-python3.10.12-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN conda install -y \
        hdbscan==0.8.33 \
        jupyterlab==4.0.9 \
        k3d==2.16.0 \
    && conda clean -ya

RUN pip3 install -U \
    matplotlib==3.8.2 \
    networkx==3.2.1 \
    numpy==1.26.2 \
    pandas==2.1.3 \
    scikit-learn==1.3.2 \
    scipy==1.11.4 \
    seaborn==0.13.0 \
    tqdm==4.66.1 \
    umap-learn==0.5.5

COPY postInstall /
RUN /postInstall
