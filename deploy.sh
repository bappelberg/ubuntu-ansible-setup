#!/bin/bash
echo "Remember to execute the following command on new VM: sudo apt update && sudo apt install openssh-server -y sudo systemctl start ssh"

echo "Enter IP address for VM (ansible_host):"
read ansible_host

echo "Enter username for SSH (ansible_user):"
read ansible_user

# Create or update inventory file with these values
cat > inventory <<EOL
[ubuntu_vms]
ubuntu-vm ansible_host=$ansible_host ansible_user=$ansible_user ansible_ssh_private_key_file=~/.ssh/id_ed25519
EOL

echo "Inventory file created/updated with following content:"
cat inventory

cat ~/.ssh/id_ed25519.pub | ssh $ansible_user@$ansible_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && chmod 700 ~/.ssh"

echo "To run ansible execute the following command: ansible-playbook -i inventory ubuntu_setup.yml --ask-become-pass"