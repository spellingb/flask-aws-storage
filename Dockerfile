FROM python:3.7-slim

ENV BUCKET_NAME=insert_bucket_name_here
ENV PACMAN_URL=localhost
RUN groupadd flaskgroup \
    && useradd -m -g flaskgroup -s /bin/bash flask \
    && mkdir -p /home/flask/app/web  \
    && mkdir /home/flask/app/web/uploads \
    && apt-get update  \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools curl \
    && rm -rf /var/lib/apt/lists/* 

WORKDIR /home/flask/app/web
COPY requirements.txt /home/flask/app/web
RUN pip install --no-cache-dir -r requirements.txt
COPY . /home/flask/app/web
# RUN npm install
RUN chown -R flask:flaskgroup /home/flask
# WORKDIR /home/flask/app/web/packman-canvas
# RUN (npm run start&) && echo "starting pacman"
# WORKDIR /home/flask/app/web
EXPOSE 5000

USER flask
ENTRYPOINT [ "python3" ]
CMD [ "-m" , "flask", "run", "--host=0.0.0.0"]
