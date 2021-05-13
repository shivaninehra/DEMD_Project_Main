<<<<<<< HEAD
web: uvicorn app:app --host 127.0.0.1 --port=${PORT:-8000}
=======
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
>>>>>>> 3916701 (Fourth Commit)
