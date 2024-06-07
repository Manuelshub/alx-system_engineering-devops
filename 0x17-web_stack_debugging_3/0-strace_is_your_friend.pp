# A puppet manifest to replace a line in a server

$filename = '/var/www/html/wp-settings.php'

#replace line containing phpp to php

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${filename}",
  path    => ['bin','usr/bin']
}
