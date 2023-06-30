.PHONY: go swagger js rust python java

all:
	docker-compose up

go:
	docker-compose run --rm chirpstack-api-go

swagger:
	@echo "swagger command is deprecated. use just 'make go' instead"

js:
	docker-compose run --rm chirpstack-api-js

rust:
	docker-compose run --rm chirpstack-api-rust

python:
	docker-compose run --rm chirpstack-api-python

java:
	docker-compose run --rm chirpstack-api-java
