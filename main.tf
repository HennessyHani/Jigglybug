provider "aws" {
    region = "eu-west-2"
}
resource "aws_instance" "demo1" {
    ami = "ami-0fb391cce7a602d1f"
    instance_type = "t2.micro"
}
