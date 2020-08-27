FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pytest
RUN pylint src/ tests/ run_from_file
RUN python run_from_file.py --movie_id 1
RUN python run_from_file.py --movie_id 220