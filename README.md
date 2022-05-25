# farm-monitoring-server

- docker run
```shell
docker build -t farm-server .

docker run -p 8000:8000 -v $PWD:/home/ec2-user --name farm-server -it farm-server /bin/bash

docker exec -it farm-server /bin/bash

docker exec -d farm-server /bin/bash
```
