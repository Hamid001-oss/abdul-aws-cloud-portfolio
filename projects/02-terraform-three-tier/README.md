# Terraform Three-Tier AWS Architecture

## Project Summary

Designed a three-tier AWS architecture using Terraform Infrastructure as Code (IaC). The goal of this project is to demonstrate how cloud infrastructure can be defined, deployed, and managed through reusable Terraform configuration.

## Architecture

The architecture separates resources into three main tiers:

1. Web Tier – receives incoming user traffic.
2. Application Tier – processes application requests.
3. Database Tier – stores application data securely.

Resources are deployed inside an Amazon VPC with public and private subnets to improve security and network isolation.

## AWS Services

- Amazon VPC
- Amazon EC2
- Application Load Balancer
- Auto Scaling
- Amazon RDS
- Security Groups
- Internet Gateway
- NAT Gateway
- Amazon CloudWatch

## Infrastructure as Code

Terraform is used to define and manage AWS infrastructure.

The infrastructure can be created consistently using:

terraform init

terraform plan

terraform apply

Terraform makes the environment repeatable and reduces the need for manual configuration in the AWS Management Console.

## Architecture Flow

Internet → Application Load Balancer → Web/Application Tier → Amazon RDS

## Key Features

- Infrastructure as Code using Terraform
- Public and private subnet architecture
- Multi-tier network design
- Load-balanced application traffic
- Auto Scaling capability
- Private database tier
- Security groups for access control
- Reusable infrastructure configuration

## Skills Demonstrated

- Terraform
- Infrastructure as Code
- AWS networking
- VPC architecture
- EC2
- Amazon RDS
- Load balancing
- Auto Scaling
- Cloud security
- Linux and AWS CLI fundamentals

## What I Learned

This project strengthened my understanding of Infrastructure as Code and three-tier AWS architecture. I learned how Terraform can be used to create repeatable cloud environments and how AWS resources can be separated into different network tiers to improve scalability, security, and manageability.
