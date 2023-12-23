# install flask from pip3
exec { 'flask':
  command  => 'pip3 install Flask==2.1.0',
  provider => 'shell'
}
