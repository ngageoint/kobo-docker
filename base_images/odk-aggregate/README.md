Building

Download the ODK Aggregate Linux x64 installer from https://opendatakit.org/downloads.

Run the installer and copy ODKAggregate.war to this directory. Sample relevant installer responses are below.

Select PostgreSQL 

```
[1] Google App Engine: Uses Google's cloud-based data storage and webserver services.
[2] MySQL: Uses a MySQL database and an Apache Tomcat 6 webserver that you install.
[3] PostgreSQL: Uses a PostgreSQL database and an Apache Tomcat 6 webserver that you install.
Please choose an option [1] : 3
```

Choose the SSL certificate option

```
[1] No, I do not have an SSL certificate:  - User logins ARE secure.
 - Submitting and/or viewing form data MAY NOT BE secure.
 - Changing passwords MAY NOT BE secure. 
Security breaches are particularly likely over unsecured WiFi hotspots.

[2] Yes, I have an SSL certificate:  - User logins ARE secure.
 - Submitting and/or viewing form data IS secure.
 - Changing passwords IS secure.

Please choose an option [1] : 2
```

Select 80/443 for ports

```
HTTP/1.1. Connector Port: [8080]: 80

HTTPS/1.1. Connector Port: [8443]: 443
```

Enter ```psql``` for the database host

```
Database server hostname: [127.0.0.1]: psql
```

