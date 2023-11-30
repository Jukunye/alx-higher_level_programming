#!/bin/bash
# Sends a POST request with variables.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
