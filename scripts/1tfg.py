import subprocess
import docker

# Open VS Code
subprocess.run(['code','.'])

# Open Intellij Idea
subprocess.run(['intellij-idea-ultimate'])

# Run mySQL in docker container
client = docker.from_env()
client.containers.run("mysql:latest", "sleep infinity", detach=True)