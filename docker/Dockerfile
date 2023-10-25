# FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /projects

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    swig \
    wget \
    virtualenv \
    libgl1-mesa-dev \
    libgl1-mesa-glx \
    libglew-dev \
    libc6-dev \
    libosmesa6-dev \
    patchelf \
    software-properties-common \
    gfortran \
    && apt-get install --no-install-recommends -y file g++ gcc make gdb strace ca-certificates \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get --no-install-recommends install -y python3.8-dev python3.8 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN \
  if [ -f requirements.txt ]; \
    then pip3 install -r requirements.txt; \
  elif [ `ls -1q *.txt | wc -l` == 1 ]; \
    then pip3 install -r *.txt; \
  fi

# Specify the command to run on container start
CMD ["/bin/bash"]
