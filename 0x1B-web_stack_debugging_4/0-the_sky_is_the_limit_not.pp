# enables nginx to handle more incoming traffic
# Increases users limit
exec { 'add-user-limit':
  command => 'sed -i "s/15/4000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

# restart nginx

exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
