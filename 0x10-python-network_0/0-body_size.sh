#!/usr/bin/env bash
# displays the size of the body of the response requested from passed URL.
curl -s "$1" | wc -c
