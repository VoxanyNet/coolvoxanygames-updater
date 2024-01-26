FROM python:3.10.13-bookworm

WORKDIR /usr/src/app

# make module folder
RUN mkdir coolvoxanygames_updater

# copy contents of the module to the module folder in container
COPY ./coolvoxanygames_updater ./coolvoxanygames_updater

RUN pip install -r ./coolvoxanygames_updater/requirements.txt

CMD ["python", "-m", "coolvoxanygames_updater"]
