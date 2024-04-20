# This puppet file creates a manifest that kills a process named killmenow

exec { 'pkill killmenow':
  command => '/usr/bin/pkill killmenow'
  }
