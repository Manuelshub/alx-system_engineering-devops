# This Puppet manifest is used to automate the task of creating a custom
# HTTP header response.

exec { 'update':
  command => '/usr/bin/apt-get update -y'
}
-> package { 'nginx':
  ensure => 'present'
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";"
}
-> exec { 'run':
  command => '/etc/init.d/nginx restart'
}
