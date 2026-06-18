#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "=========================================="
echo "  Démarrage du stack SQL Server + Adminer"
echo "=========================================="

if [ ! -f ".env" ]; then
    echo "ERREUR : fichier .env introuvable. Copiez .env.example en .env et ajustez les valeurs."
    exit 1
fi

source .env

docker compose up -d

echo ""
echo "Stack démarré. En attente du healthcheck SQL Server..."

timeout=120
elapsed=0
while [ $elapsed -lt $timeout ]; do
    status=$(docker inspect --format='{{.State.Health.Status}}' sqledge 2>/dev/null || echo "starting")
    if [ "$status" = "healthy" ]; then
        break
    fi
    printf "."
    sleep 5
    elapsed=$((elapsed + 5))
done
echo ""

if [ "$status" = "healthy" ]; then
    echo "SQL Server est prêt !"
else
    echo "Attention : SQL Server n'est pas encore healthy après ${timeout}s. Vérifiez les logs :"
    echo "  docker logs sqledge"
fi

echo ""
echo "------------------------------------------"
echo "  Accès Adminer : http://localhost:${ADMINER_PORT:-8080}"
echo "    Driver : MS SQL Server"
echo "    Serveur : sqledge"
echo "    Utilisateur : sa"
echo "    Mot de passe : (voir .env)"
echo "    Base : ${MSSQL_DATABASE:-DataScienceDB}"
echo "------------------------------------------"
echo ""
docker compose ps
