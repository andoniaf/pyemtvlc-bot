.RECIPEPREFIX +=
IMAGE_NAME = pyemtvlc

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
                @awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# Docker Tasks
build: ## Build the container
  docker build -t $(IMAGE_NAME) .

run: ## Run container
  docker run --name="$(IMAGE_NAME)" $(IMAGE_NAME)

stop: ## Stop and rm container
  docker stop $(IMAGE_NAME) && docker rm $(IMAGE_NAME)
