FROM python:3.5-onbuild
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]