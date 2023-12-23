# install flask from pip3
exec {'flask_install':
  command => 'pip3 install Flask==2.1.0'
}
