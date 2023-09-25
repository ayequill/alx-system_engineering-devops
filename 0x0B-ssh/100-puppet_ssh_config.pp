# Modifies the ssh config file

exec { 'Turn off passwd auth':
  command => "echo '    PasswordAuthentication no' >> /etc/ssh/ssh_config",
  path    => '/bin:/usr/bin',
}

exec { 'Declare identity file':
  command => "echo '    IdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config",
  path    => '/bin:/usr/bin',
}

