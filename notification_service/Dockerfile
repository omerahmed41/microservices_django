# Final image.
FROM python:3.9.12-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential=12.6 \
  git=1:2.20.* \
  libpq-dev=* \
  curl=* \
  libcurl4-openssl-dev=* \
  libssl-dev=* \
  unzip=* \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /main
COPY requirements.txt /main/
RUN pip install -r requirements.txt
COPY . /main/
