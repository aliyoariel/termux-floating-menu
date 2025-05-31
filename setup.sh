#!/bin/bash

# Periksa dan instal Python jika belum ada
echo "Memeriksa Python..."
if ! command -v python3 &> /dev/null; then
    echo "Python belum terinstall, menginstall..."
    pkg install python -y
else
    echo "Python sudah terinstall."
fi

# Periksa dan instal Tkinter jika belum ada
echo "Memeriksa Tkinter..."
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "Tkinter belum terinstall, menginstall..."
    pkg install python-tkinter -y
else
    echo "Tkinter sudah tersedia."
fi

# Jalankan aplikasi Floating Menu
echo "Menjalankan GUI Floating Menu..."
python3 floating_menu.py