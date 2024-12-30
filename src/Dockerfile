FROM ubuntu:noble

LABEL creator="Angelo Veltens <angelo.veltens@online.de>" mantainer="Alejandro Alonso <aalonsopersonal@gmail.com>" organization="Delegación de Alumnos UPM (da.upm.es)" version="1.0" description="Backup and restore MYSQL databases"

RUN apt-get update && \
    apt-get install cron bzip2 -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /backups

# Instalar el cliente de base de datos basado en DATABASE_CLIENT
ARG DATABASE_CLIENT
RUN if [ "$DATABASE_CLIENT" = "mariadb" ]; then \
      apt-get update && apt-get install mariadb-client -y && apt-get clean && rm -rf /var/lib/apt/lists/*; \
    else \
      apt-get update && apt-get install mysql-client -y && apt-get clean && rm -rf /var/lib/apt/lists/*; \
    fi

ENV DATABASE_CLIENT=${DATABASE_CLIENT}
ENV DATABASE_HOST=mariadb
ENV DATABASE_PORT=3306
ENV DATABASE_USER=root
ENV DATABASE_PASSWORD=password
ENV DATABASE_NAME=database
ENV BACKUP_TIME 0 3 * * *

COPY docker-entrypoint.sh /entrypoint.sh
COPY backup restore /bin/

VOLUME /backups

ENTRYPOINT ["/entrypoint.sh"]

CMD ["cron", "-f"]
