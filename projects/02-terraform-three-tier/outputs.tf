output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.portfolio_vpc.id
}

output "public_subnet_ids" {
  description = "Public subnet IDs"
  value = [
    aws_subnet.public_a.id,
    aws_subnet.public_b.id
  ]
}

output "application_subnet_ids" {
  description = "Application subnet IDs"
  value = [
    aws_subnet.app_a.id,
    aws_subnet.app_b.id
  ]
}

output "database_subnet_ids" {
  description = "Database subnet IDs"
  value = [
    aws_subnet.database_a.id,
    aws_subnet.database_b.id
  ]
}

output "load_balancer_dns_name" {
  description = "DNS name of the Application Load Balancer"
  value       = aws_lb.web.dns_name
}
