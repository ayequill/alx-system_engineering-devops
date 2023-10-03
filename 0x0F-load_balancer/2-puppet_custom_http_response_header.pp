# Install Nginx

exec {'update_system':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure   => 'installed',
  requires => Exec['update_system'],
}

file { 'index.html':
    ensure  => 'file',
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
    require => Package['nginx'],
}

file_line { 'Creating header':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => "\tadd_header X-Served-By ${hostname};",
  after   => 'server_name _;',
  require => Service['nginx'],
  notigy  => Service['nginx'],
}

# Start nginx
service { 'nginx':
  ensure => running,
  enable => true,
# require => File['default'],
}
