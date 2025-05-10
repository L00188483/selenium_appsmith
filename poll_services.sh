#!/bin/bash

set -e  # Exit immediately if any command exits with a non-zero status

docker ps


while true; do
  echo "Polling http://localhost:4444/status..."
  SELENIUM_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:4444/status || echo "000")

  echo "Polling http://localhost:8080/api/v1/health..."
  APPSMITH_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/v1/health || echo "000")

  if [[ "$SELENIUM_STATUS" == "200" && "$APPSMITH_STATUS" == "200" ]]; then
    echo "Both services are healthy (HTTP 200). Exiting loop."
    break
  fi

  echo "SELENIUM_STATUS=$SELENIUM_STATUS, APPSMITH_STATUS=$APPSMITH_STATUS"
  docker logs --tail 5 appsmith

  echo "$(date) - Sleeping for 30 seconds..."
  sleep 30
done

echo "services launched successfully"
curl -s http://localhost:4444/status
sleep 1
curl -s http://localhost:8080/api/v1/health
sleep 1

echo "check selenium can reach appsmith container:"
docker exec selenium_chrome ping appsmith
