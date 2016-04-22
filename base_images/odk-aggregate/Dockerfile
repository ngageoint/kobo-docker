FROM kobotoolbox/base-tomcat:latest

RUN apt-get -qq update && \
    apt-get -qq -y install \
        postgresql-9.3 \
        postgresql-client-9.3

COPY ./init_odk.bash /etc/my_init.d/01_init_odk.bash

RUN rm -rf webapps/*
COPY ./ODKAggregate.war webapps/ROOT.war
COPY ./server.xml conf/server.xml

EXPOSE 8443

CMD ["/sbin/my_init"]

