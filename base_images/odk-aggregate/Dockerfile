FROM kobotoolbox/base-tomcat:latest

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list' && \
	wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add - && \
	apt-get -qq update && \
    	apt-get -qq -y install \
        postgresql-9.3 \
        postgresql-client-9.3

COPY ./init_odk.bash /etc/my_init.d/01_init_odk.bash

RUN rm -rf webapps/*
COPY ./ODKAggregate.war webapps/ROOT.war
COPY ./server.xml conf/server.xml

EXPOSE 443

CMD ["/sbin/my_init"]

