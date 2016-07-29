#!/bin/bash
set -e

KOBO_PSQL_DB_USER=${KOBO_PSQL_DB_USER:-"kobo"}
KOBO_PSQL_DB_PASS=${KOBO_PSQL_DB_PASS:-"kobo"}
ODK_PSQL_DB_NAME=${ODK_PSQL_DB_NAME:-"odk_prod"}
ODK_PSQL_DB_SCHEMA=${ODK_PSQL_DB_SCHEMA:-"odk_prod"}
ODK_PSQL_DB_USER=${ODK_PSQL_DB_USER:-"odk_user"}
ODK_PSQL_DB_PASS=${ODK_PSQL_DB_PASS:-"odk_user"}

export PGPASSWORD=$KOBO_PSQL_DB_PASS

psql -U $KOBO_PSQL_DB_USER -h psql -d postgres <<< "create database \"$ODK_PSQL_DB_NAME\";" > /dev/null
psql -U $KOBO_PSQL_DB_USER -h psql -d $ODK_PSQL_DB_NAME <<< "create user \"$ODK_PSQL_DB_USER\" with unencrypted password '$ODK_PSQL_DB_PASS';" > /dev/null
psql -U $KOBO_PSQL_DB_USER -h psql -d $ODK_PSQL_DB_NAME <<< "grant all privileges on database \"$ODK_PSQL_DB_NAME\" to \"$ODK_PSQL_DB_USER\";" > /dev/null
psql -U $KOBO_PSQL_DB_USER -h psql -d $ODK_PSQL_DB_NAME <<< "alter database \"$ODK_PSQL_DB_NAME\" owner to \"$ODK_PSQL_DB_USER\";" > /dev/null
psql -U $KOBO_PSQL_DB_USER -d $ODK_PSQL_DB_NAME -h psql <<< "create schema \"$ODK_PSQL_DB_SCHEMA\";" > /dev/null
psql -U $KOBO_PSQL_DB_USER -d $ODK_PSQL_DB_NAME -h psql <<< "grant all privileges on schema \"$ODK_PSQL_DB_SCHEMA\" to \"$ODK_PSQL_DB_USER\";" > /dev/null

cat << EOF > /tmp/post_install.sql
CREATE OR REPLACE FUNCTION "$ODK_PSQL_DB_SCHEMA".create_prefixed_name_view(tblname text, prefix text, viewname text)
RETURNS void
AS \$\$
BEGIN
EXECUTE (
select 'CREATE OR REPLACE VIEW ' || viewname || ' AS SELECT ' ||
(select string_agg(quote_ident(table_name) || '.' ||
quote_ident(column_name) || ' AS ' || quote_ident(prefix || '_' ||
column_name), ', ')
from information_schema.columns
where table_name = tblname
group by table_name) ||
' FROM ' || quote_ident(tblname) || ';'
);
END
\$\$ LANGUAGE plpgsql;
EOF
psql -U $KOBO_PSQL_DB_USER -d $ODK_PSQL_DB_NAME -h psql < /tmp/post_install.sql

sed -i 's/$KEYSTORE_PASSWORD/'$KEYSTORE_PASSWORD'/g' /usr/local/tomcat/conf/server.xml
sed -i 's/$TRUSTSTORE_PASSWORD/'$TRUSTSTORE_PASSWORD'/g' /usr/local/tomcat/conf/server.xml


