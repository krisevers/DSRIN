FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

WORKDIR /projects

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \ 
  libopenmpi-dev \
  pip install --upgrade pip \
  && apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN \
  if [ -f requirements.txt ]; \
    then pip install -r requirements.txt; \
  elif [ `ls -1q *.txt | wc -l` == 1 ]; \
    then pip install -r *.txt; \
  fi

# Specify the command to run on container start
CMD ["/bin/bash"]
