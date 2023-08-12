#https://docs.docker.com/engine/reference/builder/
#docker build --rm -t demo-app-image:1.0.0 .
#docker run --name demo-app-container demo-app-image:1.0.0 -d


FROM python:3-alpine

ADD . /
ADD main.py /

RUN pip3 install asyncio

#start python with unbuffered output option to see print outputs in docker log
CMD [ "python", "-u", "main.py" ]