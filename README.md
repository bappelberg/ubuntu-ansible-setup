# Ubuntu Ansible Setup

## Prerequisites
- VM Fusion: Player Version 13.6.2 (24409261)
- python3
- ansible

## Useful tool
- https://pastbin.com

## macOS
### Getting started example (Ubuntu 24)
1. Download VM Fusion https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion
   1. Create VM ubuntu 24 VM, follow ubuntu interactive installation instructions
2. Download bootable iso for VM Fusion https://ubuntu.com/download/server/arm or https://cdimage.ubuntu.com/noble/daily-live/current/noble-desktop-arm64.iso 
3. After successful installation, use VM fusion ubuntu computer and run bootstrap.sh
   1. Remember IP-address from ubuntu computer
4. Go to back to the control node (macOS) and run deploy.sh
5. Finally run: ansible-playbook -i inventories/staging/hosts playbooks/site.yml --limit ubuntu_vms --ask-become-pass
