SHELL := /bin/bash

.PHONY: install run clean

run-gemini:
  @echo "Checking for 'venv-gemini' virtual environment..."
  @if [ ! -d "venv-gemini" ]; then \
    echo "'venv-gemini' virtual environment not found. Creating and installing dependencies..."; \
    python3 -m venv venv-gemini; \
    source venv-gemini/bin/activate && venv-gemini/bin/pip3 install -r requirements.gemini.txt; \
    echo "Installation complete!"; \
  fi
  @echo "Activating virtual environment and running the application..."
  @if [ -z "$(INPUT)" ]; then \
    echo "Error: INPUT variable is required. Usage: make run-gemini INPUT=example.pdf"; \
    exit 1; \
  fi
  source venv-gemini/bin/activate && venv-gemini/bin/python3 gemini.py -i "$(INPUT)"

clean:
  @echo "Removing virtual environment and temporary files..."
  rm -rf venv-gemini
  find . -name "__pycache__" -exec rm -rf {} +
  find . -name "*.pyc" -exec rm -f {} +