#!/bin/bash
rm -rf docs
pdoc --force -c show_source_code=False -o docs/ --html mx_utils
mv -v docs/mx_utils/* docs/
rm -rf docs/mx_utils
