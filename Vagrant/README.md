## Install Vagrant
- [download](https://developer.hashicorp.com/vagrant/downloads)
- [compatible with VirtualBox](https://developer.hashicorp.com/vagrant/docs/providers/virtualbox)

### Install VirtualBox
1. [download virtualbox deb file](https://www.virtualbox.org/wiki/Download_Old_Builds_6_1)
2. `sudo dpkg -i virtualbox.deb`


### Version
2.3.4

### Insatll with APT Package manager

```bash
sudo apt-get update
sudo apt-get install lsb-release
```

```bash
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vagrant
```

### CLI Examples
- box
  - list
  - remove

- destroy [name | id]
  - --force

- halt [name | id]
- provision [name | id]

  configure running machine.

- ssh [name | id] [-- extra_ssh_args]

- up [name | id]

- version
