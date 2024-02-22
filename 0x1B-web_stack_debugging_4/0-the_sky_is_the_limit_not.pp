# change limit of max-open-files
exec { 'max-open-file':
  command  => "sudo sed -i 's/^ULIMIT.*/ULIMIT=\"-n 15000\"/' /etc/default/nginx; sudo service nginx restart",
  provider => shell,
}
