# fix bad phpp extension to php in wordpress file

exec { 'fix-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-setting.php',
  path    => '/usr/local/bin/:/bin/'
}
