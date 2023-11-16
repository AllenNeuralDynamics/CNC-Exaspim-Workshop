# hash:sha256:26e49376d53ef3aece4af647b6e8085b974d7f67766b2eb5136de229dfd84495
FROM registry.codeocean.allenneuraldynamics.org/codeocean/jupyterlab:3.0.9-miniconda4.9.2-python3.8-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN conda install -y \
        jupyterlab==3.5.2 \
    && conda clean -ya

RUN pip install -U --no-cache-dir \
    matplotlib==3.7.3 \
    numpy==1.23.5 \
    pandas==2.0.3
