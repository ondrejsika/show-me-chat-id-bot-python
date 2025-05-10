FROM python:3.13-slim
RUN pip install --no-cache-dir --upgrade pipenv
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY . .
CMD ["pipenv", "run", "python", "main.py"]
