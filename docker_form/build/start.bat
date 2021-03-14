echo "Building kpk docker"
docker build -f ./build/docker/Dockerfile -t kpk ./build/docker/
echo "Starting kpk docker"
