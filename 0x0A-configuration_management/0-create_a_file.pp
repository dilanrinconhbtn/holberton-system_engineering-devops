# Using Puppet, create a file in /tmp.
file { '/tmp/holberton':
  path    => '/tmp/holberton', # path
  mode    => '0744',         # permissions
  owner   => 'www-data',       # owner
  group   => 'www-data',       # group
  content => 'I love Puppet',  # content
}
