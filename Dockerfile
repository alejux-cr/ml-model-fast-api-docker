FROM frolvlad/alpine-miniconda3:python3.7

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
	rm requirements.txt

EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]