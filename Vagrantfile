# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	# Base box to build off, and download URL for when it doesn't exist on the user's system already
	config.vm.box = "ubuntu/trusty32"
	config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"        

	config.vm.provider :aws do |aws, override|
        	aws.access_key_id = "AKIAIC27KBAMV4JLB2CQ"
        	aws.secret_access_key = "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"
        	aws.keypair_name = "SDSEastKey.cer"

        	aws.security_groups = ''
        	aws.region = 'us-east-1'

        	aws.ami = 'ami-896c96fe'
        	aws.instance_type = 't1.micro'

        	override.ssh.username = ENV['AWS_SSH_USER']
        	override.ssh.private_key_path = ENV['AWS_KEY_PATH']
	end
	# As an alternative to precise32, VMs can be built from the 'django-base' box as defined at
	# https://github.com/torchbox/vagrant-django-base , which has more of the necessary server config
	# baked in and thus takes less time to initialise. To go down this route, you will need to build
	# and host django-base.box yourself, and substitute your own URL below.
	#config.vm.box = "django-base-v2.2"
	#config.vm.box_url = "http://vmimages.torchbox.com/django-base-v2.2.box"  # Torchbox-internal URL to django-base.box
	
	# Boot with a GUI so you can see the screen. (Default is headless)
	# config.vm.boot_mode = :gui
	
	# Assign this VM to a host only network IP, allowing you to access it
	# via the IP.
	# config.vm.network "33.33.33.10"
	
	# Forward a port from the guest to the host, which allows for outside
	# computers to access the VM, whereas host only networking does not.
#	config.vm.forward_port 8000, 8111
	
	# Share an additional folder to the guest VM. The first argument is
	# an identifier, the second is the path on the guest to mount the
	# folder, and the third is the path on the host to the actual folder.
#	config.vm.share_folder "project", "/home/vagrant/spitfire", "."
	
	# Enable provisioning with a shell script.
	config.vm.provision :shell, :path => "etc/install/install.sh", :args => "spitfire"
end

