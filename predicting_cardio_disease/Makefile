#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = predicting_cardio_disease
PYTHON_VERSION = 3.13.1
PYTHON_INTERPRETER = python
VENV_NAME = venv

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Create a Python virtual environment
.PHONY: create_environment
create_environment:
	@echo "Creating virtual environment '$(VENV_NAME)' using Python $(PYTHON_VERSION)..."
	$(PYTHON_INTERPRETER) -m venv $(VENV_NAME)
	@echo "Virtual environment created. Activate it using:"
	@echo "  On Unix/macOS: source $(VENV_NAME)/bin/activate"
	@echo "  On Windows: $(VENV_NAME)\Scripts\activate"


## Install Python dependencies
.PHONY: requirements
requirements: create_environment
	@echo "Installing requirements from requirements.txt..."
	$(VENV_NAME)/Scripts/$(PYTHON_INTERPRETER) -m pip install -U pip
	$(VENV_NAME)/Scripts/$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	@echo "Requirements installed."


## Delete all compiled Python files
.PHONY: clean
clean:
	@echo "Cleaning up compiled Python files..."
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	@echo "Cleanup complete."


## Lint using ruff (use `make format` to do formatting)
.PHONY: lint
lint:
	@echo "Running ruff linter..."
	ruff format --check
	ruff check
	@echo "Linting complete."

## Format source code with ruff
.PHONY: format
format:
	@echo "Running ruff formatter..."
	ruff check --fix
	ruff format
	@echo "Formatting complete."



## Run tests
.PHONY: test
test:
	@echo "Running pytest..."
	$(VENV_NAME)/Scripts/$(PYTHON_INTERPRETER) -m pytest tests
	@echo "Tests finished."




#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)