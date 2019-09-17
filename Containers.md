### Configuration notes

The container build host is a registered RHEL host
docker, buildah and podman commands were aliased to "sudo COMMAND" due to the local user not having the needed rights.

### How to build the container image:
```
$ docker build . -t wipe
Sending build context to Docker daemon 193.5 kB
Step 1/5 : FROM centos:latest
 ---> 67fa590cfc1c
Step 2/5 : ADD wipe.py /
 ---> 8228ebdc438b
Removing intermediate container 7ade65c2c9cc
Step 3/5 : RUN yum install -y python-requests
 ---> Running in dc8fba9b968f

Loaded plugins: fastestmirror, ovl
Determining fastest mirrors
 * base: repos-tx.psychz.net
 * extras: repos-tx.psychz.net
 * updates: repos-tx.psychz.net
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
--------------------------------------------------------------------------------
Total                                              1.0 MB/s | 277 kB  00:00     
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
 ---> 3523cd34f0a2
Removing intermediate container dc8fba9b968f
Step 4/5 : RUN yum install -y python-libs
 ---> Running in 2746bdb6e25f

Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
 * base: repos-tx.psychz.net
 * extras: repos-tx.psychz.net
 * updates: repos-tx.psychz.net
Package python-libs-2.7.5-80.el7_6.x86_64 already installed and latest version
Nothing to do
 ---> 6ae5b493b493
Removing intermediate container 2746bdb6e25f
Step 5/5 : ENTRYPOINT python /wipe.py -ip $IP -u $USERNAME -p $PASSWORD -t $TYPE
 ---> Running in dc5c2957ea7e
 ---> 1fba7dabf074
Removing intermediate container dc5c2957ea7e
Successfully built 1fba7dabf074
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
wipe                latest              1fba7dabf074        49 seconds ago      425 MB
docker.io/centos    latest              67fa590cfc1c        3 weeks ago         202 MB
```

### How to run docker container
```
$ docker run --env IP=10.10.10.11 --env USERNAME=hope --env PASSWORD=5tr0ng --env TYPE=DELL wipe:latest
```

### How to build podman containier

Add docker.io to the registries line of /etc/containers/registries.conf
```
sudo vi /etc/containers/registries.conf
```
Build the image
```
$ buildah bud -t wipepod .
STEP 1: FROM centos:latest
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
(1/4): extras/7/x86_64/primary_db                          | 215 kB   00:00     
(2/4): base/7/x86_64/group_gz                              | 166 kB   00:00     
(3/4): updates/7/x86_64/primary_db                         | 7.4 MB   00:00     
(4/4): base/7/x86_64/primary_db                            | 6.0 MB   00:04     
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
Total                                              887 kB/s | 277 kB  00:00     
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
Copying blob sha256:b0e5bce2c0f5eb14fc089a194103cc4035cb236f1a3cfa34b6c970435e521f1d
 37.60 MiB / 37.60 MiB [====================================================] 1s
Copying config sha256:cdf20c403659f6a1bc11887e40b7ab5f289b20e6d33bd4f216003c556182c03f
 1.25 KiB / 1.25 KiB [======================================================] 0s
Writing manifest to image destination
Storing signatures
--> cdf20c403659f6a1bc11887e40b7ab5f289b20e6d33bd4f216003c556182c03f
```
### Run the podman container
```
podman run --env IP=10.10.10.11 --env USERNAME=hope --env PASSWORD=5tr0ng --env TYPE=FOO -it wipepod:latest

 Other Not Implemented Yet
```
### Build podman containier user Red Hat provided UBI image

Log into the Red Hat registry
```
$ podman login registry.access.redhat.com
Username: username@redhat.com
Password: 
Login Succeeded!
```

Pull down the wanted image
```
$ podman pull registry.access.redhat.com/ubi8/ubi
Trying to pull registry.access.redhat.com/ubi8/ubi...Getting image source signatures
Copying blob sha256:567fcfc2ff356ea53650461873c8212a964526aafa07997bd6006ccf6c8a4fe0
 67.77 MB / ? [------------------------------------------=----------------] 12s 
Copying blob sha256:188d0510bf1408baf514bd594738c95e39217cc12569c121619273bfc301c048
 1.48 KB / ? [---------------------------------=---------------------------] 0s 
Copying config sha256:a73bf97264a0284c17069ffbc2c5682619e851a1e61124cf285b9229301d5692
 4.43 KB / 4.43 KB [========================================================] 0s
Writing manifest to image destination
Storing signatures
a73bf97264a0284c17069ffbc2c5682619e851a1e61124cf285b9229301d5692
```
Build the image
```
$ buildah bud -t wipepod -f Dockerfile.podman .
STEP 1: FROM registry.access.redhat.com/ubi8/ubi
STEP 2: USER root
STEP 3: ADD wipe.py /
STEP 4: RUN yum install -y python36 python3-requests
Updating Subscription Management repositories.
Unable to read consumer identity
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
Red Hat Universal Base Image 8 (RPMs) - AppStre 300 kB/s | 1.9 MB     00:06    
Red Hat Universal Base Image 8 (RPMs) - BaseOS  142 kB/s | 754 kB     00:05    
Last metadata expiration check: 0:00:02 ago on Mon Sep 16 17:23:01 2019.
Dependencies resolved.
================================================================================
 Package            Arch   Version                        Repository       Size
================================================================================
Installing:
 python36           x86_64 3.6.8-2.module+el8.0.0.z+3769+7dd96c37
                                                          ubi-8-appstream  19 k
 python3-requests   noarch 2.20.0-1.el8                   ubi-8-baseos    123 k
Installing dependencies:
 python3-pip        noarch 9.0.3-13.el8                   ubi-8-appstream  18 k
 python3-setuptools noarch 39.2.0-4.el8                   ubi-8-baseos    162 k
 python3-urllib3    noarch 1.23-5.el8                     ubi-8-baseos    178 k
 python3-idna       noarch 2.5-5.el8                      ubi-8-baseos     97 k
 python3-pysocks    noarch 1.6.8-3.el8                    ubi-8-baseos     34 k
 python3-chardet    noarch 3.0.4-7.el8                    ubi-8-baseos    195 k
Enabling module streams:
 python36                  3.6                                                 

Transaction Summary
================================================================================
Install  8 Packages

Total download size: 828 k
Installed size: 2.9 M
Downloading Packages:
(1/8): python36-3.6.8-2.module+el8.0.0.z+3769+7  16 kB/s |  19 kB     00:01    
(2/8): python3-pip-9.0.3-13.el8.noarch.rpm       15 kB/s |  18 kB     00:01    
(3/8): python3-requests-2.20.0-1.el8.noarch.rpm  93 kB/s | 123 kB     00:01    
(4/8): python3-setuptools-39.2.0-4.el8.noarch.r 1.1 MB/s | 162 kB     00:00    
(5/8): python3-urllib3-1.23-5.el8.noarch.rpm    1.1 MB/s | 178 kB     00:00    
(6/8): python3-idna-2.5-5.el8.noarch.rpm        1.2 MB/s |  97 kB     00:00    
(7/8): python3-pysocks-1.6.8-3.el8.noarch.rpm   517 kB/s |  34 kB     00:00    
(8/8): python3-chardet-3.0.4-7.el8.noarch.rpm   1.9 MB/s | 195 kB     00:00    
--------------------------------------------------------------------------------
Total                                           561 kB/s | 828 kB     00:01     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                        1/1 
  Installing       : python3-chardet-3.0.4-7.el8.noarch                     1/8 
  Installing       : python3-pysocks-1.6.8-3.el8.noarch                     2/8 
  Installing       : python3-urllib3-1.23-5.el8.noarch                      3/8 
  Installing       : python3-idna-2.5-5.el8.noarch                          4/8 
  Installing       : python3-setuptools-39.2.0-4.el8.noarch                 5/8 
  Installing       : python3-pip-9.0.3-13.el8.noarch                        6/8 
  Installing       : python36-3.6.8-2.module+el8.0.0.z+3769+7dd96c37.x86_   7/8 
  Running scriptlet: python36-3.6.8-2.module+el8.0.0.z+3769+7dd96c37.x86_   7/8 
  Installing       : python3-requests-2.20.0-1.el8.noarch                   8/8 
  Running scriptlet: python3-requests-2.20.0-1.el8.noarch                   8/8 
  Verifying        : python36-3.6.8-2.module+el8.0.0.z+3769+7dd96c37.x86_   1/8 
  Verifying        : python3-pip-9.0.3-13.el8.noarch                        2/8 
  Verifying        : python3-requests-2.20.0-1.el8.noarch                   3/8 
  Verifying        : python3-setuptools-39.2.0-4.el8.noarch                 4/8 
  Verifying        : python3-urllib3-1.23-5.el8.noarch                      5/8 
  Verifying        : python3-idna-2.5-5.el8.noarch                          6/8 
  Verifying        : python3-pysocks-1.6.8-3.el8.noarch                     7/8 
  Verifying        : python3-chardet-3.0.4-7.el8.noarch                     8/8 
Installed products updated.

Installed:
  python36-3.6.8-2.module+el8.0.0.z+3769+7dd96c37.x86_64                        
  python3-requests-2.20.0-1.el8.noarch                                          
  python3-pip-9.0.3-13.el8.noarch                                               
  python3-setuptools-39.2.0-4.el8.noarch                                        
  python3-urllib3-1.23-5.el8.noarch                                             
  python3-idna-2.5-5.el8.noarch                                                 
  python3-pysocks-1.6.8-3.el8.noarch                                            
  python3-chardet-3.0.4-7.el8.noarch                                            

Complete!
STEP 5: ENTRYPOINT python3 /wipe.py -ip $IP -u $USERNAME -p $PASSWORD -t $TYPE
STEP 6: COMMIT containers-storage:[overlay@/var/lib/containers/storage+/var/run/containers/storage:overlay.override_kernel_check=true]localhost/wipepod:latest
Getting image source signatures
Skipping fetch of repeat blob sha256:233b26fa30c531819f161df4c41c0047b7af7b0d9e6fc187dbf5ff5eb6fb7b02
Skipping fetch of repeat blob sha256:bd38306bf343382dd09e2a108d0b8667017c32bb0739e1490198468dd4a71d5d
Copying blob sha256:e3d947830cf535ed2746d179a0bba2d3f36029cf92b58577036850fd92a3375b
 9.51 MiB / 9.51 MiB [======================================================] 0s
Copying config sha256:7ea27f3e8b6371f7c82e58d51725e4b2d536b9d61e34e1bffaa298a696560563
 2.23 KiB / 2.23 KiB [======================================================] 0s
Writing manifest to image destination
Storing signatures
--> 7ea27f3e8b6371f7c82e58d51725e4b2d536b9d61e34e1bffaa298a696560563
```

Run the image

```
$ podman run --env IP=10.10.10.11 --env USERNAME=hope --env PASSWORD=5tr0ng --env TYPE=FOO -it wipepod:latest

 Other Not Implemented Yet
```

