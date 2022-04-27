FROM python:3.9-alpine  # 目前本地开发环境是 3.9 版本

ENV PYTHONUNBUFFERED 1

# 替换为国内源
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

WORKDIR /app

# RUN pip install pipenv -i https://pypi.douban.com/simple

#COPY Pipfile /app/Pipfile
#COPY Pipfile.lock /app/Pipfile.lock
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt --system --deploy --ignore-pipfile

COPY . /app

COPY ./compose/production/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh