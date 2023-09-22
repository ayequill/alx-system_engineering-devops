# Create a file in /tmp/myschool with the following content
file { '/tmp/myschool':
  ensure  => 'file',
  mode    => '744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
