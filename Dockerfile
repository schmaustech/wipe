FROM centos:latest
ADD wipe.py /usr/local/bin
RUN PKGS="python-requests python-libs" && yum install -y --setopt=tsflags=nodocs $PKGS && yum clean all && rpm -V $PKGS
ENTRYPOINT python /usr/local/bin/wipe.py -ip $IP -u $USERNAME -p $PASSWORD -t $TYPE
