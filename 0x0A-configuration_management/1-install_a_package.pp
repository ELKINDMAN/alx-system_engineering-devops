#Installing a version of flask via Puppet

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

