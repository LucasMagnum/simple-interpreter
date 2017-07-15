clean: ## Clean environment
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

lint:  ## Lint project
	flake8

setup-tests:  ## Install python requirements
	pip install -r requirements.txt

test: clean lint  ## Run tests
	py.test . -vsx

test-coverage: clean lint  ## Run test coverage
	py.test -vsx .  --cov . --no-cov-on-fail