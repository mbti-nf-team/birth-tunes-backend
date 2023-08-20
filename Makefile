.PHONY: run-api
run-api:
	docker build . --force-rm --no-cache --tag birth-tunes-backend
	docker run -d -p 8080:8080 --env-file ./.env birth-tunes-backend:latest
