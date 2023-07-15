# Stage 1 - Build
FROM node:18 as build-deps
WORKDIR /usr/src/app
COPY ./myfront/package*.json ./
RUN npm install
COPY ./myfront ./
RUN npm run build

# Stage 2 - the production environment
FROM nginx:1.24.0-alpine
RUN ls -la
COPY --from=build-deps /usr/src/app/dist /usr/share/nginx/html/dist

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf


EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


## Stage 1 - Build
#FROM node:18 as build-deps
#WORKDIR /usr/src/app
#COPY ./myfront/package*.json ./
#RUN npm install
#COPY ./myfront ./
#RUN npm run build
#
## Stage 2 - the production environment
#FROM nginx:1.24.0-alpine
#
## Copy the build output to replace the default nginx contents.
#COPY --from=build-deps /usr/src/app/dist /usr/share/nginx/html
#
## Add the env.js file to the Docker image
#COPY ./myfront/public/env.js /usr/share/nginx/html/env.js
#
## Replace 'http://localhost:8000' in env.js with the value of VUE_APP_BACKEND_URL
#CMD ["/bin/sh", "-c", "sed -i 's|http://localhost:8000|'${VUE_APP_BACKEND_URL}'|g' /usr/share/nginx/html/env.js && exec nginx -g 'daemon off;'"]
#
## Copy the Nginx configuration file
#COPY nginx.conf /etc/nginx/nginx.conf
#
#EXPOSE 80
