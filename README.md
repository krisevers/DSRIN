# Deployment of a Python application for Data Science Research Infrastructure for Neuroscience (DSRIN)
This code serves as a template for building data science applications on a computing cluster using `OpenShift` and `Kubernetes`. This template will perform a simple GLM on a some high-dimensional toy data in parallel using multiple cluster threads (`cpus`) in parallel.

## The Approach
1. Introduce `Docker` for containerization of applications.
2. Introduce `OpenShift` and `Kurbernetes` platforms for high-performance computing (hpc).
3. Introduce `MPI` for parallel processing.
4. Introduce `SnakeMake` as an workflow tool.


### Docker

### OpenShift + Kubernetes

### SnakeMake

### MPI

## Notes
*The Python code sample uses the **8081** HTTP port.*

Before you begin creating an application with this `devfile` code sample, it's helpful to understand the relationship between the `devfile` and `Dockerfile` and how they contribute to your build. You can find these files at the following URLs:

* [Python `devfile.yaml`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/devfile.yaml)
* [Python `Dockerfile`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/docker/Dockerfile)

1. The `devfile.yaml` file has an [`image-build` component](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/devfile.yaml#L24-L30) that points to your `Dockerfile`.
2. The [`docker/Dockerfile`](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/docker/Dockerfile) contains the instructions you need to build the code sample as a container image.
3. The `devfile.yaml` [`kubernetes-deploy` component](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/devfile.yaml#L31-L44) points to a `deploy.yaml` file that contains instructions for deploying the built container image.
4. The `devfile.yaml` [`deploy` command](https://github.com/devfile-samples/devfile-sample-python-basic/blob/main/devfile.yaml#L46-L59) completes the [outerloop](https://devfile.io/docs/2.2.0/innerloop-vs-outerloop) deployment phase by pointing to the `image-build` and `kubernetes-deploy` components to create your application.

### Additional resources
* For more information about Python, see [Python](https://www.python.org/).
* For more information about devfiles, see [Devfile.io](https://devfile.io/).
* For more information about Dockerfiles, see [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).