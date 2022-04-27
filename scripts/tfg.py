import subprocess
import docker

# Open VS Code
subprocess.run(['code','/home/cfres/Codigo'])

# Open Intellij Idea
subprocess.run(['intellij-idea-ultimate-edition'])

# Run mySQL in docker container
client = docker.from_env()
client.containers.run("mysql:latest", "sleep infinity", detach=True)