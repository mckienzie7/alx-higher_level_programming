#!/bin/bash
#POST request with variables and values
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
