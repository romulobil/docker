FROM node:alpine
ENV PORT=3000
WORKDIR /usr/app
COPY . .
RUN yarn install
CMD yarn start
EXPOSE $PORT