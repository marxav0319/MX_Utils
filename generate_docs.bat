@echo off
rmdir docs /S /Q
pdoc --force -c show_source_code=False --html mx_utils -o docs
move "docs\mx_utils\*" "docs"
move "docs\mx_utils\mailer" "docs"
rmdir docs\mx_utils /S /Q
@echo on
