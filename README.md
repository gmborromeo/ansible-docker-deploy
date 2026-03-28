# 🚀 Ansible Docker App Deployer

Automates the deployment of a Python Flask web app inside a Docker container using Ansible. Fully automated — zero manual steps.

## 📋 What This Project Does

- Installs Docker on any Ubuntu/Debian server
- Builds a Docker image from source
- Deploys and runs the app in a container
- Manages secrets securely with Ansible Vault

## 🗂️ Project Structure

ansible-docker-deploy/
├── inventory/
│   └── hosts.ini        # Target servers
├── roles/
│   ├── docker/          # Installs and configures Docker
│   │   └── tasks/
│   │       └── main.yml
│   └── app/             # Deploys the Flask app
│       ├── tasks/
│       │   └── main.yml
│       └── files/
│           ├── app.py
│           └── Dockerfile
├── vars/
│   ├── main.yml         # Global variables
│   └── secrets.yml      # Encrypted secrets (Ansible Vault)
├── playbook.yml         # Main entry point
└── README.md

## ⚙️ Requirements

- Ansible 2.9+
- Python 3.x
- Target machine running Ubuntu 20.04+

## 🚀 Usage

### 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ansible-docker-deploy.git
cd ansible-docker-deploy

### 2. Update inventory
Edit `inventory/hosts.ini` with your target server IP.

### 3. Run the playbook
ansible-playbook playbook.yml -i inventory/hosts.ini --ask-vault-pass

### 4. Access the app
http://YOUR_SERVER_IP:5000

## 🔐 Secrets Management

Sensitive variables are encrypted with Ansible Vault.
To edit secrets:
ansible-vault edit vars/secrets.yml

## 📚 What I Learned

- Ansible inventory, ad-hoc commands, and playbooks
- Role-based project structure
- Docker automation with community.docker collection
- Securing secrets with Ansible Vault
- Idempotent infrastructure automation

## 🛠️ Tech Stack

- Ansible
- Docker
- Python / Flask
- Ubuntu / WSL
