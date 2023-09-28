FROM public.ecr.aws/lambda/python:3.11
COPY requirements.txt ${LAMBDA_TASK_ROOT}
COPY hello_world.py ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt
CMD [ "hello_world.just_checking" ]
# docker build command with options/flags:
# docker build --platform linux/amd64 -t hello-world:test .
# docker run command:
# docker run -p 9000:8080 --name lambda-cont hello-world:test
# This command runs the image as a container and creates a local endpoint 
# at localhost:9000/2015-03-31/functions/function/invocations.
# curl command to exeute the function:
# curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"greetings": "Hello Class!"}'