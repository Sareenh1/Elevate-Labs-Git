# Task 4: Build a Version-Controlled DevOps Project

## Objective
Manage a DevOps project using Git best practices, hosted on GitHub, and developed on an AWS EC2 t2.micro Ubuntu instance.

## Steps and Commands

### 1. Set Up EC2 Instance
- Launched a t2.micro Ubuntu 22.04 instance on AWS.
- Connected via SSH:
  ```bash
  ssh -i task4-key.pem ubuntu@<PUBLIC_IP>

###  Installed Git
  ```bash
  sudo apt update
  sudo apt install git -y

###  Configured Git
  ```bash
  git config --global user.name "Sareenh1"
  git config --global user.email "Sareenh10@gmail.com"

### 2. Create GitHub Repository
  - Created devops-task4 repository on GitHub.
  - Generated a personal access token for authentication.

### 3. Initialize Repository
###   Cloned Repository
  ```bash
  git clone https://github.com/<your-username>/devops-task4.git

- Created system_check.py for system monitoring (CPU, memory).
-Added .gitignore for Python projects.
-Wrote README.md with project details.

### Initial commit
  ```bash
  git add .
  git commit -m "Initial commit: Add system_check.py, .gitignore, and README.md"
  git push origin main

### 4.Branching Workflow

### Created dev branch
  ```bash
  git checkout -b dev
  git push origin dev

### Created feature/disk-usage branch
  ```bash
  git checkout -b feature/disk-usage

###Added disk usage to system_check.py.
###Committed and pushed:`
  ```bash
  git add system_check.py
  git commit -m "Add disk usage monitoring to system_check.py"
  git push origin feature/disk-usage

###Created PR from feature/disk-usage to dev and merged.
###Created PR from dev to main and merged.

### 5. Git Tags
  ```bash
  git tag -a v1.0.0 -m "Release 1.0.0: Initial system monitoring with CPU, memory, and disk"
  git push origin v1.0.0

### 6. Documentation
### Created this TASKS.md to document all steps.
###Updated README.md with project overview and setup instructions.
