FROM nginx
WORKDIR usr/share/nginx
USER root
RUN apt-get update
RUN apt-get install curl
EXPOSE 80
EXPOSE 80000
ADD . usr/share/nginx/html
MAINTAINER Fulano de Tal <fulano@exemplo.com>
