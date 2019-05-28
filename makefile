test:
	@echo "Building nk_sent2vec Image"
	docker-compose build
	@echo "Running Tests"
	docker-compose run nk_sent2vec pytest --color=yes -s tests
