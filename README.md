# docker-flask-boilerplate
Docker image for Flask App

## Requirements
* Docker

## Development

### Build the image
<pre>
docker build --rm -t docker-flask-boilerplate:latest .
</pre>

### Run it
<pre>
docker run -p 8000:8000 docker-flask-boilerplate:latest
</pre>

### Build and run with docker-compose
<pre>
docker-compose up --build
</pre>
