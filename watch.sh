#!/usr/bin/env bash

while inotifywait -e modify tools/api_gen.py tools/templates/; do
  uv run tools/api_gen.py
done
