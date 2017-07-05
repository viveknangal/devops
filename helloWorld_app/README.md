# Docker-Compose file for HelloWorld Application(having TLS on frontend)


##  Functionality
This **docker-compose** file spins two different containers as follows :-

1. **Frontend Container** : This container is configured to run the *Nginx* process with Self Signed certifcates & it proxy all the requests to the *Backend* container.This container accepts both https & http requests.
2. **Backend Container** : This container is configured to run the *Python SimpleHTTPServer* serving the HelloWorld page.This container accepts traffic from the Frontend container on http.

**Docker Images in the above docker-compose file have been created & pushed to my personal DockerHub account**

## Usage
1. Download the "docker-compose" file in a directory
2. Execute the Below command
```hcl
docker-compose up
```
3. Browse the below URL in the browser 
```hcl
https://localhost:8082
```

## Result
Once the above URL is accessed the below content is displayed on the browser

```hcl

This is a Hello World APp served by container = <BACKEND_CONTAINER_ID>
```
