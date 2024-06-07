# A puppet manifest to replace a line in a server

$file_to_edit = '/var/www/html/wp-settings.php'

#replace line containing phpp to php

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
