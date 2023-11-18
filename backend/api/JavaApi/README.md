# JavaApi

## Running the application in dev mode

You can run your application in dev mode that enables live coding using:
```shell script
./mvnw compile quarkus:dev
```
# TODO: change it to docker-compose with auto dnative build

## Running the kubernetes cluster 

To initially run, setup your cluster, and run 
```shell script
kubectl apply -f stateless-api-deployment.yml
```

To update the api version, run
```shell script
kubectl rollout restart deployment api-deployment -n java-api
```
