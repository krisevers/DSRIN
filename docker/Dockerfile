FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

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
