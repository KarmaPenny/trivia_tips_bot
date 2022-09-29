FROM public.ecr.aws/lambda/python:3.9
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt
COPY src/ ./
CMD [ "main.main" ]
