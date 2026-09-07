FROM python:3.13-slim
WORKDIR /app
COPY pyproject.toml .
COPY src/ ./src/
RUN python -m pip install .
CMD ["python", "-m", "flask", "--app", "src.api", "run", "--host=0.0.0.0"]