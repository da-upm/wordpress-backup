#!/bin/bash

if ! [ -f backup-cron ]
then
  echo "Creating cron entry to start backup at: $BACKUP_TIME"
  # Note: Must use tabs with indented 'here' scripts.
  cat <<-EOF >> backup-cron
DATABASE_HOST=$DATABASE_HOST
DATABASE_USER=$DATABASE_USER
DATABASE_NAME=$DATABASE_NAME
DATABASE_PASSWORD=$DATABASE_PASSWORD
EOF

  if [[ $CLEANUP_OLDER_THAN ]]
  then
    echo "CLEANUP_OLDER_THAN=$CLEANUP_OLDER_THAN" >> backup-cron
  fi
  echo "$BACKUP_TIME backup > /backup.log" >> backup-cron

  crontab backup-cron
fi

echo "Current crontab:"

mount -t davfs https://drive.upm.es/public.php/webdav /backups

crontab -l

exec "$@"
