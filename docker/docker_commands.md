# Docker Commands Reference

## Basic Docker Commands

### Container Management
```bash
# List running containers
docker ps

# List all containers (running and stopped)
docker ps -a

# Run a container
docker run <image_name>

# Run a container in detached mode
docker run -d <image_name>

# Stop a container
docker stop <container_id>

# Start a stopped container
docker start <container_id>

# Remove a container
docker rm <container_id>

# Execute command in running container
docker exec -it <container_id> /bin/bash
```

### Image Management
```bash
# List images
docker images

# Pull an image
docker pull <image_name>

# Build an image from Dockerfile
docker build -t <image_name> .

# Remove an image
docker rmi <image_id>
```

### Docker Compose
```bash
# Start services
docker-compose up

# Start services in detached mode
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs
```

## Cleanup Commands (Use with caution!)

### Stop all running containers
```bash
docker stop $(docker ps -q)
```
**Explanation:** Stops all currently running containers. `docker ps -q` returns only container IDs, and `$()` executes the command and uses its output.

### Remove all containers
```bash
docker rm $(docker ps -aq)
```
**Explanation:** Removes all containers (both running and stopped). `-a` flag includes stopped containers, `-q` returns only IDs.

### Remove all images
```bash
docker rmi $(docker images -q)
```
**Explanation:** Removes all Docker images from the system. This will free up significant disk space but requires re-downloading images when needed.

### Remove all volumes
```bash
docker volume rm $(docker volume ls -q)
```
**Explanation:** Removes all Docker volumes. **Warning:** This will delete all persistent data stored in volumes.

### Complete system cleanup
```bash
docker system prune --all
```
**Explanation:** Removes all unused containers, networks, images, and build cache. The `--all` flag removes all unused images, not just dangling ones.

## ⚠️ Important Notes
- The cleanup commands will remove data permanently
- Always backup important data before running cleanup commands
- Use `docker system df` to check disk usage before cleanup
- Consider using `docker system prune` without `--all` for safer cleanup