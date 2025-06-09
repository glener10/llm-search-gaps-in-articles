SHELL := /bin/bash

.PHONY: install run test clean

#Install dependencies of all llms
install:
	@echo "Creating and activating virtual environment..."
	python3 -m venv venv
	@echo "Installing dependencies..."
	source venv/bin/activate && pip3 install -r requirements.txt
	@echo "Installation complete!"

run-gemini:
	@echo "Starting the application..."
	@if [ -z "$(INPUT)" ]; then \
		echo "Error: INPUT variable is required for run-gemini. Usage: make run-gemini INPUT=example.pdf"; \
		exit 1; \
	fi
	source venv/bin/activate && python3 gemini.py -i "$(INPUT)"

clean:
	@echo "Removing virtual environment and temporary files..."
	rm -rf venv
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +