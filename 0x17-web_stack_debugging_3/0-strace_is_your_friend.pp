# this puppet will fix a typo in wp settings file
file {  '/var/www/html/wp-settings.php':
  ensure => present,
}->
file_line { 'change php to phpp':
  path => '/var/www/html/wp-settings.php',
  line => 'require_once( ABSPATH . WPINC . '/class-wp-locale.php' );',
  match => 'require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );',
}
