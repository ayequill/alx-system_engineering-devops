# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# exec { 'change_ownership':
#   command => 'sudo chown -R siaw:siaw /var/www/html',
#   path    => '/usr/bin',
#   require => Package['nginx'],
# }

# Create index.html
file { 'index.html':
    ensure  => 'file',
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
    require => Package['nginx'],
}

# Create 404.html
file { '404':
    ensure  => 'file',
    path    => '/var/www/html/404.html',
    content => 'Ceci n\'est pas une page',
    require => Package['nginx'],
}

# Modify default nginx config
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

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}
	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files \$uri \$uri/ =404;
	}

	error_page 404 /404.html;
	location = /404.html {
		root /var/www/html;
		internal;
	}

}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Start nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['default'],
}
