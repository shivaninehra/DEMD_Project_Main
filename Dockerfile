<<<<<<< HEAD
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY Pulsar_star_pickle.pkl /app
COPY main.py /app
=======
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY Pulsar_star_pickle.pkl /app
COPY app.py /app
>>>>>>> 3916701 (Fourth Commit)