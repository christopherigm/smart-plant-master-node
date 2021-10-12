# Social Events Platform API

### Attach bluetooth

[Reference](https://velog.io/@kitsunetic/Serial-Communication-using-Python-Linux-through-BLE-with-Arduino-HC-06)
```sh
sudo rfcomm bind 0 00:14:03:05:0C:5D
```

## Build and push Docker image
```sh
docker build -t smart-plant .
```

### Tag Docker image
```sh
docker tag smart-plant longmont.iguzman.com.mx:5000/smart-plant:1.0
```

### Push Docker image
```sh
docker push longmont.iguzman.com.mx:5000/smart-plant:1.0
```

## Run Docker image

### Pull docker image
```sh
docker pull longmont.iguzman.com.mx:5000/smart-plant:1.0
```

### Test it
```sh
docker run -p 8000:8000 --name smart-plant --privileged longmont.iguzman.com.mx:5000/smart-plant:1.0
```

### Run it for ever
```sh
docker run -d -p 8000:8000 --name smart-plant --restart=always --privileged longmont.iguzman.com.mx:5000/smart-plant:1.0 
```

### Stop it and remove it
```sh
docker stop smart-plant
docker rm smart-plant
```

### Clean docker containers
```sh
docker rm $(docker ps -a -f status=exited -q)
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```
