# FROM domblack/oracle-jre8
FROM anapsix/alpine-java:8_server-jre_unlimited
MAINTAINER Adfinis SyGroup/Namics

# RUN yum install -y epel-release && yum clean all
# RUN yum install -y --enablerepo=centosplus \
#       libselinux-devel \
#       httpd \
#       wget \
#       zip \
#       python-psutil \
#       python-pycurl \
#     && yum clean all
# RUN yum install -y epel-release && yum clean all
RUN apk update
RUN apk add ca-certificates
RUN update-ca-certificates
RUN apk add wget \
      zip \
      python \
      py-psutil \
      py-curl
# libselinux-devel \
      # httpd \
    # && yum clean all

# Install utility for AEM
COPY aemInstaller.py /aem/aemInstaller.py
# COPY files/license.properties /aem/license.properties
# COPY files/AEM_6.3_Quickstart.jar /aem/AEM_6.3_Quickstart.jar
