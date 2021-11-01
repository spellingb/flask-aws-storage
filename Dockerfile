FROM python:3.7-slim

RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

RUN mkdir -p /home/flask/app/web
RUN mkdir /home/flask/app/web/uploads
WORKDIR /home/flask/app/web

COPY requirements.txt /home/flask/app/web
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/flask/app/web

RUN chown -R flask:flaskgroup /home/flask

EXPOSE 5000
ENV BUCKET_NAME=insert_bucket_name_here
USER flask
ENTRYPOINT [ "python3" ]
CMD [ "-m" , "flask", "run", "--host=0.0.0.0"]