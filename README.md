# Abraxas DevOps Exercise

## Get your environment ready

You'll need:

1. A Github account
2. A docker hub account
3. Access to a kubernetes cluster for testing purposes (I love [K3s](https://github.com/rancher/k3s)! Because is very simple setup a cluster for testing or developemnt in five minutes you have K8s running in docker.)
4. Clone this repository locally.

## Solutions

This sections describe the solutions.


### Dockerize services

Dockerize the given service at [app.py](app.py), including all it's required dependencies installed and ready to rock.

For this point only copy *py and requirement.txt and this version include the extra point. 
The extra point, extend the function hello() and save "counter" in redis, this solution allows scale up and scale down the pods with app.py and save in a one sigle place. Of course, this value only persists in lifecicle of the pod but you can attach a volumen for resolve this issue.



### CI/CD

Implement a Github Actions workflow to build and publish your docker image on [docker hub](https://hub.docker.com/).
This solution only build the image when you commit and push on master and result image is r2d2r2d2/exercise:latest and i don't kwnow why not is funcionality with the git tags.

### Deployment

Create a service configuration file to deploy the service on your kubernetes cluster and expose it to the world.
The repository includes 2 solutions, K8s/manisfests/v1/ and K8s/manifests/v2/ both implement the extra point.

- [K8s/manifests/v1](https://github.com/arthur-rock/devops-exercise/tree/master/K8s/manifests/v1)
	- **a-namespace.yml.** Create a namespace devops-exercise
	- **b-redis.yml.** Define a pod with a instance redis in namespace devops-exercise.
	- **c-devops-exercise.yml.** Define a Deployment with 2 replicas in namespace devops-exercise. 
	- You can see running with the next command (sudo only for k3s):
	`sudo kubectl apply -f v1
	
    Output expected:
	namespace/devops-exercise created
	pod/redis created
	service/redis created
	deployment.apps/devops-exercise created
	service/devops-exercise created
	`
	- ** After minutes, you can exec next commands **
	`sudo kubectl get svc/devops-exercise --namespace="devops-exercise" -o wide| tail -n +2| awk '{print $3":"$5}'| awk -F: '{print "curl -X GET http://"$1":"$2"\ncurl -X POST "$1":"$2}'
	
	Output expected:
	curl -X GET http://10.43.40.215:8080
	curl -X POST 10.43.40.215:8080
	`
	The ip is the ClusterIp associated with the svc. 
	Or you can replace that ip for any ip of the cluster and remember use the port 31000 because the svc associated is the type NodePort.

- [K8s/manifests/v2](https://github.com/arthur-rock/devops-exercise/tree/master/K8s/manifests/v2)
	- a-namespace.yml. Create a namespace devops-exercise
	- b-configMap-nginx.yml. Create a configMap for nginx, this configMap contain the minimum directives like upstream  and hide nginx version.
	- c-redis-counter.yml. Define a pod with a instance redis in namespace devops-exercise.
	- d-multicontainer-devops-exercise.yml. Define multicontainer Deployment, all request through nginx and nginx make request to app server.
	You can see running with the next command (sudo only for k3s):
	`sudo kubectl apply -f v2`

  

### Extra Points

- Improve the given python service so it maintains a counter of the amount of **POST** requests it served, and return it on **GET** requests.
The extra point, extend the function hello() and save "counter" in redis, this solution allows scale up and scale down the pods with app.py and save in a one sigle place. Of course, this value only persists in lifecicle of the pod but you can attach a volumen for resolve this issue. 


## Deliverables

- A link to the public docker registry where the image is published.
  [Docker registry](https://hub.docker.com/repository/docker/r2d2r2d2/exercise)

- A link to your repository containing:

    1. The Dockerfile(s) for the image(s).
    2. The kubernetes file(s) for the service deployment(s). The deployment should be replicable on our kubernetes cluster.
    3. Optionally the code for the improved version of the service.
	[Repository](https://github.com/arthur-rock/devops-exercise)

## General Guidelines

Your code should be as simple as possible, yet well documented and robust.
Spend some time on designing your solution. Think about operational use cases from the real world. Few examples:

1. What happens if a service crashes?
2. How much effort will it take to create a new service? D.R.Y!

## Reference

- [Run a Stateless Application Using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)

