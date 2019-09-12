FROM centos:latest
ADD wipe.py /
RUN yum install -y python-requests
RUN yum install -y python-libs
#RUN chmod +x /wipe.py
#ENV IP=10.10.10.10
#ENV USERNAME=bob
#ENV PASSWORD=secret
#ENV TYPE=something
ENTRYPOINT python /wipe.py -ip $IP -u $USERNAME -p $PASSWORD -t $TYPE
