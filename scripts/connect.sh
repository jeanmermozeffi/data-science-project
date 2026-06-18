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

echo "Connexion à SQL Server via isql (sa@${MSSQL_DATABASE:-DataScienceDB})..."
echo "Tapez votre requête SQL puis appuyez sur Entrée. Quittez avec 'quit'."
docker exec -it sqledge isql -v \
    -k "Driver={ODBC Driver 17 for SQL Server};Server=localhost,1433;UID=sa;PWD=${MSSQL_SA_PASSWORD};Database=${MSSQL_DATABASE:-DataScienceDB};TrustServerCertificate=Yes;"
