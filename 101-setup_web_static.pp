#!/usr/bin/env bash
# Configure server using puppet

# defines a Puppet class called nginx_server
class nginx_server {
  package { 'nginx':
    ensure => installed,
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => directory,
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  content => '<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>',
  ensure  => file,
}

# Create or recreate the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Give ownership of the /data/ folder to the ubuntu user AND group
file { '/data':
  owner => 'ubuntu',
  group => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
file_line { 'nginx_config':
  path   => '/etc/nginx/sites-available/default',
  line   => "        location /hbnb_static {\n            alias /data/web_static/current;\n        }",
  before => '}',
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  notify    => File_line['nginx_config'],
}
