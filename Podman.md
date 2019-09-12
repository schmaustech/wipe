# How to build the podman container
```
buildah bud -t wipepod .
STEP 1: FROM centos:latest
Getting image source signatures
Copying blob sha256:d8d02d45731499028db01b6fa35475f91d230628b4e25fab8e3c015594dc3261
 71.92 MiB / 71.92 MiB [====================================================] 3s
Copying config sha256:67fa590cfc1c207c30b837528373f819f6262c884b7e69118d060a0c04d70ab8
 2.13 KiB / 2.13 KiB [======================================================] 0s
Writing manifest to image destination
Storing signatures
STEP 2: ADD wipe.py /
STEP 3: RUN yum install -y python-requests
Loaded plugins: fastestmirror, ovl
Determining fastest mirrors
 * base: mirror.dal10.us.leaseweb.net
 * extras: mirror.dal10.us.leaseweb.net
 * updates: mirror.dal10.us.leaseweb.net
base                                                     | 3.6 kB     00:00     
extras                                                   | 3.4 kB     00:00     
updates                                                  | 3.4 kB     00:00     
(1/4): base/7/x86_64/group_gz                              | 166 kB   00:00     
(2/4): extras/7/x86_64/primary_db                          | 215 kB   00:00     
(3/4): updates/7/x86_64/primary_db                         | 7.4 MB   00:00     
(4/4): base/7/x86_64/primary_db                            | 6.0 MB   00:00     
Resolving Dependencies
--> Running transaction check
---> Package python-requests.noarch 0:2.6.0-1.el7_1 will be installed
--> Processing Dependency: python-urllib3 >= 1.10.2-1 for package: python-requests-2.6.0-1.el7_1.noarch
--> Running transaction check
---> Package python-urllib3.noarch 0:1.10.2-5.el7 will be installed
--> Processing Dependency: python-six for package: python-urllib3-1.10.2-5.el7.noarch
--> Processing Dependency: python-ipaddress for package: python-urllib3-1.10.2-5.el7.noarch
--> Processing Dependency: python-backports-ssl_match_hostname for package: python-urllib3-1.10.2-5.el7.noarch
--> Running transaction check
---> Package python-backports-ssl_match_hostname.noarch 0:3.5.0.1-1.el7 will be installed
--> Processing Dependency: python-backports for package: python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch
---> Package python-ipaddress.noarch 0:1.0.16-2.el7 will be installed
---> Package python-six.noarch 0:1.9.0-2.el7 will be installed
--> Running transaction check
---> Package python-backports.x86_64 0:1.0-8.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                               Arch     Version            Repository
                                                                           Size
================================================================================
Installing:
 python-requests                       noarch   2.6.0-1.el7_1      base    94 k
Installing for dependencies:
 python-backports                      x86_64   1.0-8.el7          base   5.8 k
 python-backports-ssl_match_hostname   noarch   3.5.0.1-1.el7      base    13 k
 python-ipaddress                      noarch   1.0.16-2.el7       base    34 k
 python-six                            noarch   1.9.0-2.el7        base    29 k
 python-urllib3                        noarch   1.10.2-5.el7       base   102 k

Transaction Summary
================================================================================
Install  1 Package (+5 Dependent packages)

Total download size: 277 k
Installed size: 1.0 M
Downloading packages:
warning: /var/cache/yum/x86_64/7/base/packages/python-backports-1.0-8.el7.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID f4a80eb5: NOKEY
Public key for python-backports-1.0-8.el7.x86_64.rpm is not installed
(1/6): python-backports-1.0-8.el7.x86_64.rpm               | 5.8 kB   00:00     
(2/6): python-backports-ssl_match_hostname-3.5.0.1-1.el7.n |  13 kB   00:00     
(3/6): python-ipaddress-1.0.16-2.el7.noarch.rpm            |  34 kB   00:00     
(4/6): python-six-1.9.0-2.el7.noarch.rpm                   |  29 kB   00:00     
(5/6): python-requests-2.6.0-1.el7_1.noarch.rpm            |  94 kB   00:00     
(6/6): python-urllib3-1.10.2-5.el7.noarch.rpm              | 102 kB   00:00     
--------------------------------------------------------------------------------
Total                                              984 kB/s | 277 kB  00:00     
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
Importing GPG key 0xF4A80EB5:
 Userid     : "CentOS-7 Key (CentOS 7 Official Signing Key) <security@centos.org>"
 Fingerprint: 6341 ab27 53d7 8a78 a7c2 7bb1 24c6 a8a7 f4a8 0eb5
 Package    : centos-release-7-6.1810.2.el7.centos.x86_64 (@CentOS)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : python-ipaddress-1.0.16-2.el7.noarch                         1/6 
  Installing : python-six-1.9.0-2.el7.noarch                                2/6 
  Installing : python-backports-1.0-8.el7.x86_64                            3/6 
  Installing : python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch     4/6 
  Installing : python-urllib3-1.10.2-5.el7.noarch                           5/6 
  Installing : python-requests-2.6.0-1.el7_1.noarch                         6/6 
  Verifying  : python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch     1/6 
  Verifying  : python-requests-2.6.0-1.el7_1.noarch                         2/6 
  Verifying  : python-backports-1.0-8.el7.x86_64                            3/6 
  Verifying  : python-ipaddress-1.0.16-2.el7.noarch                         4/6 
  Verifying  : python-six-1.9.0-2.el7.noarch                                5/6 
  Verifying  : python-urllib3-1.10.2-5.el7.noarch                           6/6 

Installed:
  python-requests.noarch 0:2.6.0-1.el7_1                                        

Dependency Installed:
  python-backports.x86_64 0:1.0-8.el7                                           
  python-backports-ssl_match_hostname.noarch 0:3.5.0.1-1.el7                    
  python-ipaddress.noarch 0:1.0.16-2.el7                                        
  python-six.noarch 0:1.9.0-2.el7                                               
  python-urllib3.noarch 0:1.10.2-5.el7                                          

Complete!
STEP 4: RUN yum install -y python-libs
Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
 * base: mirror.dal10.us.leaseweb.net
 * extras: mirror.dal10.us.leaseweb.net
 * updates: mirror.dal10.us.leaseweb.net
Package python-libs-2.7.5-80.el7_6.x86_64 already installed and latest version
Nothing to do
STEP 5: ENTRYPOINT python /wipe.py -ip $IP -u $USERNAME -p $PASSWORD -t $TYPE
STEP 6: COMMIT containers-storage:[overlay@/var/lib/containers/storage+/var/run/containers/storage:overlay.override_kernel_check=true]localhost/wipepod:latest
Getting image source signatures
Skipping fetch of repeat blob sha256:877b494a9f30e74e61b441ed84bb74b14e66fb9cc321d83f3a8a19c60d078654
Copying blob sha256:6067f34bfcfb9b8c95b7ec449f3a95a27ced49707a28baa099fa99ac65be6530
 37.60 MiB / 37.60 MiB [====================================================] 1s
Copying config sha256:6cfa10d60aaeb45870ff5cdaaac7f2a29ea399adc0be624faf964e21b6899b81
 1.25 KiB / 1.25 KiB [======================================================] 0s
Writing manifest to image destination
Storing signatures
--> 6cfa10d60aaeb45870ff5cdaaac7f2a29ea399adc0be624faf964e21b6899b81
```

# List the podman images
```
$ sudo podman images
REPOSITORY                 TAG      IMAGE ID       CREATED         SIZE
localhost/wipepod          latest   6cfa10d60aae   3 minutes ago   322MB
docker.io/library/centos   latest   67fa590cfc1c   3 weeks ago     210MB
```

# How to run the podman image
```
sudo podman run --env IP=10.10.10.11 --env USERNAME=hope --env PASSWORD=5tr0ng --env TYPE=DELL wipepod:latest
```
