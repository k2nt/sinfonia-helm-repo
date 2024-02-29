#!/bin/bash

# Get the parent directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Packaging Helm charts..."

# Package all Helm charts in the 'charts' folder
for chart in "$SCRIPT_DIR"/../charts/*; do
    if [ -d "$chart" ]; then
        chart_name=$(basename "$chart")
        helm package "$chart" -d "$PARENT_DIR" > /dev/null
        echo "Packaged $chart_name"
    fi
done

echo "All Helm charts packaged successfully!"


echo "Rebuiding index.yaml..."

# Rebuild the index.yaml file
helm repo index .

echo "Rebuiding index.yaml done!"
