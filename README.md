# flask_app
This repo was created to learn RESTAPI and Flask python

How to deploy flask server? Flow steps below
Step1:
    - Execute "make build_image" to build falsk image with name "flask_python"

Step2:
    - Execute "make run_image" to start falsk server
    - if user wants to restart container use "make rerun_startup"

*Note: User need to install Docker before deploy the falsk server


…or push an existing repository from the command line
git remote add origin https://github.com/tiennguyen047/fast_api.git
git branch -M main
git push -u origin main