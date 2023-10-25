FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive

# Install packages
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

# Install MPI
RUN wget -q http://www.mpich.org/static/downloads/3.1.4/mpich-3.1.4.tar.gz
RUN tar xfz mpich-3.1.4.tar.gz
WORKDIR mpich-3.1.4
RUN ./configure --disable-fortran --enable-fast=all,03 --prefix=/usr
RUN make -j$(nproc)
RUN make install
RUN ldconfig
WORKDIR /

# Setup environment
ENV VIRTUAL_ENV=/venv 
RUN virtualenv --python=python3.8 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python packages
RUN \
  if [ -f requirements.txt ]; \
    then pip install -r requirements.txt; \
  elif [ `ls -1q *.txt | wc -l` == 1 ]; \
    then pip install -r *.txt; \
  fi

# Copy the content of the local src directory to the working directory
COPY . .

# Clean up the pip cache
RUN pip cache purge

# Specify the command to run on container start
CMD ["/bin/bash"]
