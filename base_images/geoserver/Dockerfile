FROM kobotoolbox/base-tomcat:latest

ENV GEOSERVER_VERSION=2.8.3
ENV GEOSERVER_URL http://sourceforge.net/projects/geoserver/files/GeoServer/$GEOSERVER_VERSION/geoserver-$GEOSERVER_VERSION-war.zip
RUN curl -fSL $GEOSERVER_URL -o geoserver-war.zip \
        && rm -rf webapps/* \
        && unzip -j geoserver-war.zip geoserver.war -d webapps \
        && mv webapps/geoserver.war webapps/ROOT.war \
        && rm geoserver-war.zip

VOLUME ["/srv/geoserver"]
EXPOSE 8080

CMD ["/sbin/my_init"]

