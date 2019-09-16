FROM centos:latest
ADD wipe.py /
RUN yum install -y python-requests
RUN yum install -y python-libs
ENTRYPOINT python /wipe.py -ip $IP -u $USERNAME -p $PASSWORD -t $TYPE
