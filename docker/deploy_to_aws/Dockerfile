FROM public.ecr.aws/lambda/python:3.11
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt
COPY hello_class.py ${LAMBDA_TASK_ROOT}
CMD [ "hello_class.say_hello" ]