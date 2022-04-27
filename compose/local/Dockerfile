FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

# 替换为国内源
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update \
  # Pillow dependencies
  && apk add libffi-dev gcc g++ jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN apk add python3-dev


WORKDIR /app

# RUN pip install pipenv -i https://pypi.douban.com/simple

#COPY Pipfile /app/Pipfile
#COPY Pipfile.lock /app/Pipfile.lock
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple


COPY ./compose/local/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh