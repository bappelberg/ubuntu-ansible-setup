# Ubuntu Ansible Setup

## Prerequisites
- VM Fusion: Player Version 13.6.2 (24409261)
   - Bridged (Wi-Fi)
- python3
- ansible

## Useful tool
- https://pastbin.com

## macOS
### Getting started example (Ubuntu 24)
1. Download VM Fusion https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion
2. Download bootable iso for VM Fusion https://ubuntu.com/download/server/arm or https://cdimage.ubuntu.com/noble/daily-live/current/noble-desktop-arm64.iso 
4. Create VM ubuntu 24 VM, follow ubuntu interactive installation instructions
   1. username: mallard
   2. password: qwerty
5. Set network to Bridged (Wi-Fi) in VMWare fusion
6. After successful installation. Reboot machine as instructed, press enter and login with mallard and qwerty
7. run ```sudo apt update && sudo apt upgrade -y sudo apt autoremove -y && sudo apt clean```
8. run ```sudo apt install ssh -y  && sudo systemctl start ssh``` 
9. Open VMWare Fusion>Window>mallard: Network Adapter copy ip-address-> 123.45.67.89
10. Switch to the control node (macOS) and run deploy.sh --ip 123.45.67.89  --user mallard
11. Finally run: ansible-playbook -i inventories/staging/hosts playbooks/site.yml --limit ubuntu_vms --ask-become-pass
