FROM ubuntu

LABEL creator="Angelo Veltens <angelo.veltens@online.de>" mantainer="Alejandro Alonso <aalonsopersonal@gmail.com>" organization="Delegación de Alumnos UPM (da.upm.es)" version="1.0" description="Backup and restore MYSQL databases"


RUN apt-get update && \
    apt-get install mysql-client mariadb-client cron bzip2 -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /backups

ENV DATABASE_CLIENT mariadb
ENV DATABASE_HOST mariadb
ENV DATABASE_PORT 3306
ENV DATABASE_USER root
ENV DATABASE_PASSWORD password
ENV DATABASE_NAME database
ENV BACKUP_TIME 0 3 * * *

COPY docker-entrypoint.sh /entrypoint.sh
COPY backup restore /bin/

VOLUME /backups

ENTRYPOINT ["/entrypoint.sh"]

CMD ["cron", "-f"]
