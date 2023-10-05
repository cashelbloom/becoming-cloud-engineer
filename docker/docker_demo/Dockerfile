FROM public.ecr.aws/lambda/python:3.11
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt
ENV DDB_TABLE_NAME=ship_data_table
COPY ship.py ${LAMBDA_TASK_ROOT}
COPY ship_function.py ${LAMBDA_TASK_ROOT}
CMD [ "ship_function.lambda_handler" ]