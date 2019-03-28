#!/usr/bin/env sh
# Based on: https://github.com/pollosp/ruby-docker/blob/master/test.sh
echo "Lintering..."
# https://github.com/hadolint/hadolint
#docker run --rm -i hadolint/hadolint hadolint --ignore DL3018 - < Dockerfile && echo "Lintering OK"
docker run --rm -i hadolint/hadolint hadolint - < Dockerfile && echo "Lintering OK"

