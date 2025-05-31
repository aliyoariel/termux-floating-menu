#!/bin/bash

# Cek apakah paket sudah terinstall
function check_pkg() {
    dpkg -s "$1" &> /dev/null
}

echo "Memeriksa dependensi..."

# Daftar paket yang diperlukan
packages=("termux-x11" "xdotool" "wmctrl" "python")

for pkg in "${packages[@]}"; do
    if check_pkg "$pkg"; then
        echo "$pkg sudah terinstall, dilewati."
    else
        echo "Menginstall $pkg..."
        pkg install "$pkg" -y
    fi
done

# Cek apakah PyGObject sudah terinstall
if python -c "import gi" 2>/dev/null; then
    echo "PyGObject sudah terinstall, dilewati."
else
    echo "Menginstall PyGObject..."
    pip install PyGObject
fi

# Jalankan GUI
echo "Menjalankan aplikasi GUI..."
python floating_menu.py