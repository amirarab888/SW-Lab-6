#!/bin/bash
echo "Testing load balancer..."

for i in {1..3}; do
    echo "Test $i:"
    curl -sS http://localhost:8080/health || echo "Failed"
    echo
done

docker ps | grep interface
