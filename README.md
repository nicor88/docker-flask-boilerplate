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


## AWS ECR
It's possible to push your image to AWS ECR simply calling a script in this repo.

It requires some setup:
* setup an ENV variable `$AWS_ACCOUNT`, containing the your AWS account number
* setup an ENV variable `$AWS_DEFAULT_REGION`, containing the your AWS account number
* install `awscli` 
* configure your credentails in `~/.aws/credentials`
* make sure that your AWS IAM user it's able to push to ECR
* run the command:
	<pre>
	bash scripts/push_to_ecr.sh your_repo_name
	</pre>