# hash:sha256:ad628c7839f0b0cfa1754c2e671b222b9e5d32efb8901ab368922f532d02927f
FROM registry.codeocean.allenneuraldynamics.org/codeocean/mambaforge3:23.1.0-4-python3.10.12-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN conda install -y \
        jupyterlab==4.0.9 \
    && conda clean -ya

RUN pip3 install -U \
    matplotlib==3.8.2 \
    networkx==3.2.1 \
    numpy==1.26.2 \
    pandas==2.1.3 \
    scikit-learn==1.3.2 \
    scipy==1.11.4
