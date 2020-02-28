# Sky is the limit
exec { 'Correct file and restart':
  command  => 'sudo sed -i \'s/15/30000/\' /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}