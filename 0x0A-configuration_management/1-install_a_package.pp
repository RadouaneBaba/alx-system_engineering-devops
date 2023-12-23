# install flask from pip3
exec {'pip3':
  command  => 'pip3 install Flask==2.1.0',
  provider => 'shell'
}
