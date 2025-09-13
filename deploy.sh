#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --ip)
            ansible_host="$2"
            shift 2
            ;;
        --user)
            ansible_user="$2"
            shift 2
            ;;
        *)
            echo "Okänt argument: $1"
            exit 1
            ;;
    esac
done

# Create or update inventory file with these values
cat > inventories/staging/hosts <<EOL
[ubuntu_vms]
ubuntu-vm ansible_host=$ansible_host ansible_user=$ansible_user ansible_ssh_private_key_file=~/.ssh/id_ed25519
EOL

echo "Inventory file created/updated with following content:"
cat inventories/staging/hosts

ssh-copy-id "$ansible_user@$ansible_host"
# scp "${SCRIPT_DIR}/bootstrap.sh" "${ansible_user}@${ansible_host}:/home/${ansible_user}", not possbile, need to activate ssh

echo "#### VMWARE fusion debug tips ####"
echo "1. ubuntu> Configure ssh:  sudo apt update && sudo apt install openssh-server -y && sudo systemctl enable ssh "
echo "2. macOS> Bridge network: VMWARE tabs>Virtual Machine>Network Adapter>Bridged WiFi"
