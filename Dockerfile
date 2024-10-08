# set the python version as a build-time argument with Python 3.12 as the default
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# create a virtual environment
RUN python -m venv /opt/venv

# set the virtual environment as the current location
ENV PATH=/opt/venv/bin:$PATH

# upgrade pip
RUN pip install --upgrade pip

# set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install os dependencies for mini vm
RUN apt-get update && apt-get install -y \
    # for postgres
    libpq-dev \
    # for Pillow
    libjpeg-dev \
    # for CairoSVG
    libcairo2 \
    # other
    gcc \
    && rm -rf /var/lib/apt/lists/*

# create the mini vm's code directory
RUN mkdir -p /code

# set the working directory to that same code directory
WORKDIR /code

# copy the requirements file into the container
COPY requirements.txt /tmp/requirements.txt

# copy the project code into the container's working directory
COPY ./src /code

# install the Python project requirements
RUN pip install -r /tmp/requirements.txt

# add the Django environment variables (fixes deployment issue on Railway)
# these environment variables are set as build arguments and used for configuring Django settings
ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

ARG DJANGO_DEBUG=0
ENV DJANGO_DEBUG=${DJANGO_DEBUG}

# database isn't available during build
# run any other commands that do not need the database such as:
RUN python manage.py pullstatic
RUN python manage.py collectstatic --noinput

# set the Django default project name
ARG PROJECT_NAME="rapidsaas"
 
# create a bash script to run the Django project
# this script will execute at runtime when the container starts and the database is available
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "gunicorn ${PROJECT_NAME}.wsgi:application --bind \"0.0.0.0:\$RUN_PORT\"\n" >> ./paracord_runner.sh

# make the bash script executable
RUN chmod +x paracord_runner.sh

# clean up apt cache to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# run the Django project via the runtime script when the container starts
CMD ./paracord_runner.sh
