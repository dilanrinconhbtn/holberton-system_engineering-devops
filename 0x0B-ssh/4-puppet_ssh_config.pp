# ssh Client configuration file
exec { 'n':
  command  => 'echo "    PasswordAuthentication no\n    IdentityFile ~/.ssh/holberton\n" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
