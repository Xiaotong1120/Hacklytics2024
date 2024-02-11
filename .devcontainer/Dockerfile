# Use the official image as a parent image.
FROM ubuntu:22.04

# Update the system
RUN apt-get -y update && apt-get install -y bash \
    build-essential \
    wget \
    make \
    git \
    curl \
    sudo \
    ca-certificates \
    poppler-utils \
    python3 \
    python3-pip \
    nodejs \
    npm && \
    rm -rf /var/lib/apt/lists/*

# Install python packages
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir \
    jupyter \
    jupyterlab \
    pandas \
    matplotlib \
    numpy \
    scikit-learn \
    seaborn \
    ipywidgets \
    widgetsnbextension \
    jupyter_contrib_nbextensions \
    jupyter_nbextensions_configurator \
    jupyterlab-git \
    gradio \
    streamlit \
    nb-clean \
    nbdime \
    nbdev

# Enable jupyter nbextension
# RUN jupyter nbextension enable --py widgetsnbextension

COPY requirements.txt /tmp/
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

# Run nbdev_install_quarto
RUN sudo nbdev_install_quarto

# Copy the Google Cloud credentials JSON file into the Docker image
# Make sure to place your credentials JSON file in the context directory of the Docker build or adjust the source path as necessary
COPY ./hacklytics_credentials.json /etc/google-cloud/hacklytics_credentials.json

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the credentials file inside the container
ENV GOOGLE_APPLICATION_CREDENTIALS=/etc/google-cloud/hacklytics_credentials.json


# Indicate the Dockerfile owner
LABEL maintainer="Xiaotong 'Brandon' Ma"

# Command to run on container start
CMD [ "/bin/bash" ]
