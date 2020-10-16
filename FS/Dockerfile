# ss13449 lab 3 submission
FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g ss13449 nyu

# Set up a working folder and install the pre-reqs
WORKDIR /app
RUN pip install Flask
RUN pip install requests
RUN pip install Flask-API

USER ss13449
COPY --chown=ss13449:nyu . .
CMD [ "python", "./fs.py" ]