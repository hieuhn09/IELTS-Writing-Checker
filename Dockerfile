FROM python:3.9
WORKDIR /app/ielts_checker
COPY ielts_checker .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]