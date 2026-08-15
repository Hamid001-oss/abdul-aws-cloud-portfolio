# AWS Monitoring & Security

## Project Summary

Designed an AWS monitoring and security architecture to demonstrate how cloud resources can be monitored, audited, and protected using AWS security and observability services.
## Architecture Diagram

![AWS Monitoring & Security Architecture](diagram6.jpg)

## Architecture

Amazon CloudWatch monitors AWS resources and application performance. CloudTrail records AWS account activity and API actions for auditing. Amazon SNS can send notifications when CloudWatch alarms are triggered. IAM controls access to AWS resources using users, roles, and policies.

## AWS Services

- Amazon CloudWatch
- AWS CloudTrail
- Amazon SNS
- AWS IAM
- Amazon EC2
- Amazon VPC

## Monitoring Workflow

1. AWS resources generate metrics and logs.
2. CloudWatch collects monitoring information.
3. CloudWatch alarms detect configured conditions.
4. Amazon SNS can send alert notifications.
5. CloudTrail records account and API activity for auditing.

## Security Practices

- Apply least-privilege IAM permissions
- Use IAM roles instead of hard-coded credentials
- Enable logging and monitoring
- Monitor important account activity
- Restrict network access with security groups
- Protect sensitive information and credentials
- Review CloudTrail logs for auditing

## Skills Demonstrated

- AWS monitoring concepts
- CloudWatch metrics and alarms
- CloudTrail auditing
- SNS notifications
- IAM access control
- AWS security best practices
- Cloud infrastructure monitoring

## Project Status

Portfolio demonstration project documenting an AWS monitoring and security architecture.
