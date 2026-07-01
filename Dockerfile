FROM python:3.9
WORKDIR /app
COPY the_Game.py .
CMD ["python", "the_Game.py"]
