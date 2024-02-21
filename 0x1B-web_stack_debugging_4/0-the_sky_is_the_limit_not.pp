exec { 'max-open-file':
  command => "/bin/sed -i 's/^ULIMIT.*/ULIMIT=\"-n 4096\"/' /etc/default/nginx; /usr/bin/service nginx restart",
}
