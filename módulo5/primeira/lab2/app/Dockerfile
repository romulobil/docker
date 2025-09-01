FROM node:alpine
ENV PORT=3000
WORKDIR /usr/app
COPY . .
RUN yarn install
EXPOSE $PORT
CMD yarn start
