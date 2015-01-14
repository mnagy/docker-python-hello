FROM fedora:21

# Install python twisted and clean up the cache
RUN yum -y install python-twisted && \
    yum clean all -y

# Copy twisted directory into the container image
ADD ./twisted /opt/twisted

# Expose port
EXPOSE 1337

CMD /opt/twisted/hello.py
