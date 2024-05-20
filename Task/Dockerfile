# 1- install base image 

FROM python:3.10-slim-bullseye

# 2- show logs 

ENV PYTHONBUFFERED = 1

#  3 - updaate kernel and install dependencies

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    netcat

# 4 - create workdir

WORKDIR /app

# 5- copy req
COPY requirements.txt /app/requirements.txt

# 6- install req

RUN pip install -r requirements.txt

# 7- copy files 

COPY . /app/

# 8- Ensure the entrypoint script has execution permissions

RUN chmod +x /app/entrypoint.sh



# 9- Specify the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

