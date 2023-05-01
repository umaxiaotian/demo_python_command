FROM almalinux:8.7
USER root

RUN dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN dnf update

RUN dnf -y install python39 python39-devel python3-pip
RUN dnf -y install langpacks-ja glibc-langpack-ja.x86_64
RUN dnf install -y vim less patchelf gcc

RUN mkdir -p /root/src
COPY requirements.txt /root/src
WORKDIR /root/src

RUN pip3.9 install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt