FROM python:3.8 AS build_demo

ENV no_proxy=localhost

RUN mkdir /demo_app
RUN mkdir /demo_app/logs
RUN mkdir /demo_app/logs/gunicorn


WORKDIR /demo_app
COPY ./app /demo_app/app
COPY ./etc /demo_app/etc
COPY ./scripts /demo_app/scripts
COPY ./run_*.py /demo_app/

RUN /bin/bash ./scripts/create_venv.sh
RUN /bin/bash ./scripts/install_requirements.sh

FROM python:3.8

WORKDIR /demo_app
COPY --from=build_demo /demo_app ./

RUN ls -la /
RUN ls -al /demo_app