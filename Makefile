# Backend #
install-backend:
	# Install Required Packages
	pip install --upgrade pip && pip install -r requirements.txt

format-backend:
	# Format code with Black
	black *.py backend/.

lint-backend:
	# Lint code with PyLint
	pylint *.py backend/.
	
test-backend:
	# Test code with PyTest
	# python -m pytest --cov=mylib testfile.py

build-backend:
	# Build code with Github Actions for Continuous Integration
	# docker build -t fastapi-wiki .

run-backend:
	# Docker Run
	# docker run -p 127.0.0.1:8080:8080 b19ef7dfd01b

deploy-backend:
	# Deploy using AWS ECR (Elastic Container Registry)

all-backend:
	# combine all the needed steps in build in production
	# make format lint

# FRONTEND #
install-frontend:
	# Install Required Packages

format-frontend:
	# Format code

lint-frontend:
	# Lint code
	
test-frontend:
	# Test

build-frontend:
	# Docker Build

run-frontend:
	# Docker Run

deploy-frontend:
	# Deploy using AWS ECR (Elastic Container Registry)

all-frontend:
	# combine all the needed steps in build in production
	# make format lint