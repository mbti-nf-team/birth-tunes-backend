.PHONY: build
build:
	docker build . --force-rm --no-cache --tag birth-tunes-backend
	docker run -d -p 8081:8080 --env-file ./.env birth-tunes-backend:latest

.PHONY: down
down:
	docker stop $(shell docker ps -q --filter ancestor=birth-tunes-backend:latest)
