# Create a file in /tmp/myschool with the following content

file { 'school':
  ensure  => 'file',
  path    => '/tmp/myschool',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
