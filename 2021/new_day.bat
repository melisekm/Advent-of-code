wsl bash -c "cp -a template/. day$(find . -maxdepth 1 -type d | awk 'END {print NR-1}')"
::wsl bash -c "python3 ../get_input.py --day=$(find . -maxdepth 1 -type d | awk 'END {print NR-2}')"