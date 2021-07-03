# onecareer-plus-backend

# Command
## Build and Run
docker build -t test:v1 .

docker run -d -p 5000:5000 test:v1

### you can access via localhost:5000

# Check and manage images
docker images

docker rmi test:v1

# Check container
docker ps (-a)

docker stop (CONTAINER ID)

docker rm (CONTAINER ID)
