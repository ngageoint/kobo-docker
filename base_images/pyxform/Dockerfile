FROM kobotoolbox/base:latest

RUN apt-get -qq update && \
    apt-get -qq -y install \
        libxml2-dev \
        libxslt1-dev \
        python-dev \
        python-lxml \
        openjdk-8-jdk \
        python-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install -e git+https://github.com/XLSForm/pyxform.git@master#egg=pyxform

WORKDIR /src/pyxform/pyxform

