FROM python:bullseye

COPY ./requirements.txt /requirements.txt
COPY ./core /app
COPY ./core/media /vol/media
COPY ./run.sh /run.sh


WORKDIR /app

EXPOSE 8000

ENV PYTHONBUFFERED 1

RUN pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home appuser && \
    mkdir -p /vol/static && \
    mkdir -p /vol/media && \
    chown -R appuser:appuser /vol && \
    chmod -R 755 /vol

# run as root
CMD ["/run.sh"]

# compose cmd run as appuser
USER appuser