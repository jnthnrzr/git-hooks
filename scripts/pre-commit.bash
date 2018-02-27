#!/usr/bin/env bash

echo "Running pre-commit hook"
./scripts/run-tests.bash

# $? stores exit value of the last command
if [ $? -ne 0 ]; then
    echo "Commit FAILURE: Tests must pass before commit!"
    exit 1
else
    echo "Commit SUCCESS: All tests passed!"
    exit 0
fi
