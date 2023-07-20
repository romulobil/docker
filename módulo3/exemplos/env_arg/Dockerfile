FROM nginx
COPY index.html /usr/share/nginx/html
ARG NOME_ARG=fulano
ENV NOME_ENV="DOCKER"
#ENV NOME_ENV=${NOME_ARG}
RUN sed -i "s|Hello World|Oi $NOME_ARG|g" /usr/share/nginx/html/index.html