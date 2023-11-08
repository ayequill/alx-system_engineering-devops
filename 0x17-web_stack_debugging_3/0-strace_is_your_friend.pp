# Edits the wp-settings file

exec {'fix_wp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
