
SRC_DIR = src

rerun_startup:
	@docker restart flask_app

build_image: Dockerfile
	@echo "Build Flask image"
	@docker build -t flask_python .

USER=$$(whoami)
run_image:
	@docker run -d -it -p 5000:5000 --user=$(USER) --name=flask_app -v /home/$(USER)/python_study/flask_app/src:/home/flask/flaskapp  flask_python bash
