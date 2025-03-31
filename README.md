libvirt-exporter
=========

Install the [libvirt-exporter](https://github.com/inovex/prometheus-libvirt-exporter) which is still maintained and not archived or deprecated.

Requirements
------------

you need libvirt installed and running on the hosts with and the socket /var/run/libvirt/libvirt-sock available.

Role Variables
--------------

Variable can be found in `defaults/main.yml` and are as follows: [Click here](defaults/main.yml)

Dependencies
------------

Example Playbook
----------------

    - hosts: hypervisor
      roles:
         - { role: msterhuj.libvirt_exporter }

Run molecule tests
------------------

```bash
git clone git@github.com:msterhuj/ansible-role-libvirt-exporter.git -b master msterhuj.libvirt_exporter
cd msterhuj.libvirt_exporter
poetry install
poetry run molecule test
```

License
-------

GNU GPLv3

Author Information
------------------

msterhuj
