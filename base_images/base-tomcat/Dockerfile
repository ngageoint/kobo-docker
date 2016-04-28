FROM kobotoolbox/base:latest

RUN apt-get -qq update && \
    apt-get -qq -y install \
        openjdk-7-jdk \
        wget \
        libssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz

ENV APR_VERSION 1.5.2
ENV APR_TGZ_URL http://apache.cs.utah.edu/apr/apr-$APR_VERSION.tar.gz
ENV APR_HOME /usr/local/apr

RUN set -x \
    && mkdir $APR_HOME \
    && cd $APR_HOME \
    && curl -fSL "$APR_TGZ_URL" -o apr.tar.gz \
    && tar -xvf apr.tar.gz --strip-components=1 \
    && ./configure \
    && make \
    && make install \
    && /bin/rm apr.tar.gz

ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $JAVA_HOME/bin:$CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS
RUN set -ex \
	&& for key in \
		05AB33110949707C93A279E3D3EFE6B686867BA6 \
		07E48665A34DCAFAE522E5E6266191C37C037D42 \
		47309207D818FFD8DCD3F83F1931D684307A10A5 \
		541FBE7D8F78B25E055DDEE13C370389288584E7 \
		61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \
		79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \
		80FF76D88A969FE46108558A80B953A041E49465 \
		8B39757B1D8A994DF2433ED58B3A601F08C975E5 \
		A27677289986DB50844682F8ACB77FC2E86E29AC \
		A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \
		B3F49CD3B9BD2996DA90F817ED3873F5D3262722 \
		DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \
		F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \
		F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23 \
	; do \
		gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	done

ENV TOMCAT_MAJOR 6
ENV TOMCAT_VERSION 6.0.45
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz

RUN set -x \
        && groupadd tomcat \
        && useradd -s /bin/sh -g tomcat -d $CATALINA_HOME tomcat \
	&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \
	&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \
	&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
        && tar xf bin/tomcat-native.tar.gz \
        && cd tomcat-native-1.1.34-src/jni/native \
        && ./configure --prefix $CATALINA_HOME \
        && make \
        && make install \
        && echo /usr/local/apr/lib > /etc/ld.so.conf.d/apr.conf \
        && ldconfig \
        && cd $CATALINA_HOME \ 
	&& rm bin/*.bat \
	&& rm tomcat.tar.gz* \
        && chown -R tomcat.tomcat *

COPY ./tomcat_startup.sh /etc/my_init.d/01_tomcat_startup.sh

