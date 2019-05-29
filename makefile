test:
	@echo "Building nk_sent2vec Image"
	docker-compose build nk_sent2vec
	@echo "Running Tests"
	docker-compose run nk_sent2vec pytest --color=yes -s tests

test-d3m:
	@echo "Building d3m_sent2vec Image"
	docker-compose build d3m_sent2vec
	@echo "Running Tests"
	docker-compose run d3m_sent2vec pytest --color=yes -s tests
