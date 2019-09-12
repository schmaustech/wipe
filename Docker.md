How to build the container image:
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

*** How to run the container
```
$ docker run --env IP=10.10.10.11 --env USERNAME=hope --env PASSWORD=5tr0ng --env TYPE=DELL wipe:latest
```
