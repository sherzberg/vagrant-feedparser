
$script = <<SCRIPT
cd /vagrant
sudo apt-get install -y python-pip
sudo pip install -r requirements.txt
python tests.py
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://dl.dropbox.com/u/1537815/precise64.box"
  
  #config.vm.box = "quantal64"
  #config.vm.box_url = "https://github.com/downloads/roderik/VagrantQuantal64Box/quantal64.box"

  config.vm.network :forwarded_port, guest: 8000, host: 8000

  config.vm.provision :shell, :inline => $script
  
end
