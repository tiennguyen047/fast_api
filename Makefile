
SRC_DIR = src
USER=$$(whoami)

rerun_startup:
	@docker restart flask_app

build_image: Dockerfile
	@echo "Build Flask image"
	@docker build --build-arg DEFAULT_USER=${USER} -t flask_python .

run_image:
	@docker run -d -it -p 5000:5000 --name=flask_app  flask_python bash
