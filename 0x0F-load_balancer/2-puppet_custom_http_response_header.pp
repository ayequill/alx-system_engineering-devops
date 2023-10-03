# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# exec { 'change_ownership':
#   command => 'sudo chown -R siaw:siaw /var/www/html',
#   path    => '/usr/bin',
#   require => Package['nginx'],
# }

file { 'default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-enabled/default',
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;
	
	add_header X-Served-By \$hostname;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files \$uri \$uri/ =404;
	}
}",

  notify  => Service['nginx'],
}

# Start nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['default'],
}
