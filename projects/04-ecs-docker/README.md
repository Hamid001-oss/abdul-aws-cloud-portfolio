# Docker Container Deployment on Amazon ECS

## Project Summary

Designed a containerized application deployment architecture using Docker and Amazon Elastic Container Service (ECS). This project demonstrates how applications can be packaged into Docker containers and deployed using AWS container services.

## Architecture

The application is packaged as a Docker image. The image is stored in Amazon Elastic Container Registry (ECR) and deployed through Amazon ECS.

ECS manages the application containers, while AWS networking and security services control access to the application.

## AWS Services

- Amazon ECS
- Amazon ECR
- Amazon VPC
- Application Load Balancer
- Amazon CloudWatch
- AWS IAM
- Security Groups

## Technologies

- Docker
- Amazon ECS
- Amazon ECR
- Linux
- AWS CLI

## Architecture Flow

Application Code → Docker Image → Amazon ECR → Amazon ECS → Application Load Balancer → Users

## Key Features

- Docker containerization
- Container image storage with Amazon ECR
- Container orchestration with Amazon ECS
- Load-balanced application traffic
- IAM-based access control
- Security group protection
- CloudWatch logging and monitoring
- Scalable container architecture

## Skills Demonstrated

- Docker
- Amazon ECS
- Amazon ECR
- Containerization
- AWS networking
- IAM
- CloudWatch
- Load balancing
- AWS CLI
- Linux fundamentals

## What I Learned

This project strengthened my understanding of containers and cloud-based application deployment. I learned how Docker
