#! /bin/sh

rm -rf docs/shelf
mkdir docs/shelf
cp docs/shelf-index.md docs/shelf/index.md

pushd ../emscript-content/workspace > /dev/null
emscript markdown -p em.core -o ../../emscript/emscript-docs/docs/shelf
emscript markdown -p ti.cc23xx -o ../../emscript/emscript-docs/docs/shelf
popd > /dev/null
