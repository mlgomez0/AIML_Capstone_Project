FROM python:3.10-slim

WORKDIR /api
COPY ./api /api
COPY ./requirements.txt /api
COPY ./start_service.sh /api

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["/bin/bash", "start_service.sh"]