.PHONY: notebook docs
.EXPORT_ALL_VARIABLES:

activate:
	@echo "Activating virtual environment"
	poetry shell

setup: initialize_git install

test:
	pytest

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache