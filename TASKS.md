# Task 4: Build a Version-Controlled DevOps Project

## Objective
Manage a DevOps project using Git best practices, hosted on GitHub, and developed on an AWS EC2 t2.micro Ubuntu instance.

## Steps and Commands

### 1. Set Up EC2 Instance
- Launched a t2.micro Ubuntu 22.04 instance on AWS
- Connected via SSH:

```bash
ssh -i task4-key.pem ubuntu@<PUBLIC_IP>
```

### 2. Install and Configure Git

#### Install Git
```bash
sudo apt update
sudo apt install git -y
```

#### Configure Git
```bash
git config --global user.name "Sareenh1"
git config --global user.email "Sareenh10@gmail.com"
```

### 3. Create and Initialize Repository
- Created devops-task4 repository on GitHub
- Generated personal access token

#### Clone Repository
```bash
git clone https://github.com/<your-username>/devops-task4.git
```

- Created files:
  - system_check.py (system monitoring)
  - .gitignore (for Python)
  - README.md (project docs)

#### Initial Commit
```bash
git add .
git commit -m "Initial commit: Add system_check.py, .gitignore, and README.md"
git push origin main
```

### 4. Branching Workflow

#### Create Development Branch
```bash
git checkout -b dev
git push origin dev
```

#### Create Feature Branch
```bash
git checkout -b feature/disk-usage
```

- Added disk monitoring to system_check.py
- Pushed changes:

```bash
git add system_check.py
git commit -m "Add disk usage monitoring"
git push origin feature/disk-usage
```

- Merged via PRs: feature → dev → main

### 5. Create Release Tag
```bash
git tag -a v1.0.0 -m "Initial release with system monitoring"
git push origin v1.0.0
```

### 6. Documentation
- Created TASKS.md (this file)
- Updated README.md
