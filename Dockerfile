FROM python:bullseye

COPY ./requirements.txt /requirements.txt
COPY ./core /app
COPY ./core/media /vol/media
COPY ./run.sh /run.sh


WORKDIR /app

EXPOSE 8000

ENV PYTHONBUFFERED 1

RUN pip install -r /requirements.txt && \
    # create a non-root user to be used in /run.sh file
    adduser --disabled-password --no-create-home appuser && \
    chmod +x /run.sh
    
CMD ["/run.sh"]

