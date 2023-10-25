ARG PYTHON_VERSION=3.8
FROM continuumio/miniconda3

LABEL author="Kris Evers"
LABEL email="k.evers@maastrichtuniversity.nl"
LABEL image="DSRIN_image"
LABEL version="0.1"

RUN mkdir -p /home/dsrin 
RUN apt-get -y install git 

RUN conda install python=$PYTHON_VERSION

RUN conda create --name dsrin python=$PYTHON_VERSION --file requirements.txt

WORKDIR /home/dsrin

# Specify the command to run on container start
CMD ["/bin/bash"]
EXPOSE 8888