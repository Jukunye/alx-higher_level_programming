#!/bin/bash
# Sends a JSON POST request in a given file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
