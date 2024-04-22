# This puppet file makes changes to our configuration file
# so that one can connect to the server without password.

include stdlib

file_line { 'ssh_private_key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile\s+~\/\.ssh\/id_rsa$',
  replace            => true,
  append_on_no_match => true
}

file_line { 'password_auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication\s+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}
