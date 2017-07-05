# Python utility for Docker


## Script Functionality
* This script intends to find the running containers on the local machine , fetch the respective Docker image details from it & then query the 
Docker registry(Docker Hub) for finding out whether the new versions are available for the required Image.


## Usage
Run the script as follows:-

```hcl
./docker_containers.py
```

## Output
Script output the results as follows

```hcl
CONTAINER ID          TAG          UPDATE REQUIRED?
3a9ecf3438         latest         FALSE
28bb051197         latest         FALSE
```
The last column in the above output confirms whether a latest version is available for the required Container Image or not
