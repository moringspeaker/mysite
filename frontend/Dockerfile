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
COPY --from=build-deps /usr/src/app/dist /usr/share/nginx/html

# Copy the Nginx configuration file
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

