#!/bin/bash
for i in {1..10}; do
    curl -s localhost/health
    echo ""
done
