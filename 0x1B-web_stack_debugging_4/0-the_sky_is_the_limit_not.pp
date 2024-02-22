# change limit of max-open-files
exec { 'max-open-file':
  command => "/bin/sed -i 's/^ULIMIT.*/ULIMIT=\"-n 15000\"/' /etc/default/nginx; /usr/bin/service nginx restart",
}
