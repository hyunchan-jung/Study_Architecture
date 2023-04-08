## Install Ansible

### Insatll with PYPI

```bash
sudo apt-get update
sudo apt-get install python3.9 python3-pip

python3.9 -m pip install -U pip
python3.9 -m pip install ansible==7.4.0
```

## Register ssh key
```bash
ssh-keygen -t rsa
ssh-copy-id <remote-host-user>@<remote-host-ip>
```

## Ping test
```bash
ansible -i hosts.ini -m ping all
```
