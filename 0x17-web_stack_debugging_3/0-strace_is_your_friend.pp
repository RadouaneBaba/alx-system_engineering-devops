# this puppet will fix a typo in wp settings file
exec { '/var/www/html/wp-settings.php':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
