FROM python:3.10-slim

ARG PYTHON_ENV=my_env

ENV PYTHON_ENV=$PYTHON_ENV

RUN mkdir requirements

COPY requirements.txt set_python_env.sh /requirements/

RUN apt-get update && \
    apt-get install tree && \
    apt-get install -y --no-install-recommends \
        awscli \
        && \
    rm -rf /var/lib/apt/lists/*


RUN bash ./requirements/set_python_env.sh $PYTHON_ENV


# pyenv update
# pyenv install 3.12:latest

# file:///home/rafael/jobs/fastcourse/htmlcov/index.html


# test = "pytest -s -x --cov=fast_zero -vv"
# post_test = "coverage html"