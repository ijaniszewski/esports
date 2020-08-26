FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python src/run_from_file.py -m 1