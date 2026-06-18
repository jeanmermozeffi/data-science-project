#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

if [ ! -f ".env" ]; then
    echo "ERREUR : fichier .env introuvable."
    exit 1
fi

source .env

DB="${MSSQL_DATABASE:-DataScienceDB}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${DB}_${TIMESTAMP}.bak"
CONTAINER_PATH="/var/opt/mssql/backup/${BACKUP_FILE}"
LOCAL_PATH="${PROJECT_DIR}/backups/${BACKUP_FILE}"

echo "Sauvegarde de la base ${DB}..."

# Créer le dossier backup dans le container si nécessaire
docker exec sqledge mkdir -p /var/opt/mssql/backup

# Exécuter le backup SQL Server
docker exec sqledge /opt/mssql-tools/bin/sqlcmd \
    -S localhost -U sa -P "${MSSQL_SA_PASSWORD}" \
    -Q "BACKUP DATABASE [${DB}] TO DISK = N'${CONTAINER_PATH}' WITH NOFORMAT, INIT, NAME = N'${DB}-Full', SKIP, NOREWIND, NOUNLOAD, STATS = 10"

# Copier le fichier .bak vers le répertoire local
docker cp "sqledge:${CONTAINER_PATH}" "${LOCAL_PATH}"

echo "Backup créé : backups/${BACKUP_FILE}"
