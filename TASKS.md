# Task 4: Build a Version-Controlled DevOps Project

## Objective
Manage a DevOps project using Git best practices, hosted on GitHub, and developed on an AWS EC2 t2.micro Ubuntu instance.

## Steps and Commands

### 1. Set Up EC2 Instance
- Launched a t2.micro Ubuntu 22.04 instance on AWS.
- Connected via SSH:
  ```bash
  ssh -i task4-key.pem ubuntu@<PUBLIC_IP>

### 2. Installed Git
  '''bash
  sudo apt update
  sudo apt install git -y
