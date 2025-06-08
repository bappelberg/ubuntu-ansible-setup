#!/bin/bash

echo "Enter IP address for VM (ansible_host; hostname -I | awk '{print $1}' in ubuntu vm):"
read ansible_host

echo "Enter ubuntu user for SSH (ansible_user; whoami in ubuntu vm):"
read ansible_user

# Create or update inventory file with these values
cat > inventories/staging/hosts <<EOL
[ubuntu_vms]
ubuntu-vm ansible_host=$ansible_host ansible_user=$ansible_user ansible_ssh_private_key_file=~/.ssh/id_ed25519
EOL

echo "Inventory file created/updated with following content:"
cat inventories/staging/hosts

ssh-copy-id "$ansible_user@$ansible_host"

echo "#### VMWARE fusion debug tips ####"
echo "1. ubuntu> Configure ssh:  sudo apt update && sudo apt install openssh-server -y && sudo systemctl enable ssh "
echo "2. macOS> Bridge network: VMWARE tabs>Virtual Machine>Network Adapter>Bridged WiFi"
