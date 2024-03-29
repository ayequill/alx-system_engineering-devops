# Install Nginx

exec {'update_system':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure   => 'installed',
	require => Exec['update_system']
}


file { 'index.html':
    ensure  => 'file',
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
    require => Package['nginx'],
}

file { 'default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  content => "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name _;
	
	add_header X-Served-By \$hostname;

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		try_files \$uri \$uri/ =404;
	}
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Start nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
# require => File['default'],
}
