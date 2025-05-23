# python-simple-webapp

## Локальная сборка и запуск
```bash
# Сбилдить и запустить приложение с тегом 1.0.0
docker build -f ./Dockerfile -t python-simple-webapp:1.0.0 --no-cache .
docker run -d --rm --name test-app -p 8080:8080 python-simple-webapp:1.0.0

# Сбилдить и запустить приложение с тегом 2.0.0
docker build -f ./Dockerfile -t python-simple-webapp:2.0.0 --no-cache .
docker run -d --rm --name test-app2 -p 8081:8080 python-simple-webapp:2.0.0
```
