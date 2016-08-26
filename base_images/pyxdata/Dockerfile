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

RUN pip install Cython
RUN pip install -e git+https://github.com/jswhit/pyproj.git@master#egg=pyproj
RUN pip install -e git+https://github.com/hobu/mgrs.git@master#egg=mgrs
RUN pip install -e git+https://github.com/python-excel/xlrd.git@master#egg=xlrd

COPY scripts/convert_data.py /

