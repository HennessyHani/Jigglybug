output "vm_public_ip" {
    value = aws_instance.<instance label>.public_ip
}
