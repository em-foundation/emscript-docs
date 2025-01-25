#! /bin/sh

rm -rf docs/shelf
mkdir docs/shelf
cp docs/shelf-index.md docs/shelf/index.md

zigem markdown -w ../zigem-sdk/workspace/ -p em.core -o docs/shelf --delay 100
zigem markdown -w ../zigem-sdk/workspace/ -p ti.cc23xx -o docs/shelf --delay 100
