#!/usr/bin/env bash

while inotifywait -e modify tools/generate.py tools/templates; do
  uv run tools/generate.py
done
