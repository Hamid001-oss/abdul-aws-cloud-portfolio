variable "aws_region" {
  description = "AWS region used for the project"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name used to identify project resources"
  type        = string
  default     = "terraform-three-tier"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}
