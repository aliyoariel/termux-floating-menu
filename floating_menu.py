import gi
import subprocess  # Untuk eksekusi perintah sistem

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FloatingMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="Mod Menu Termux")
        
        self.set_default_size(220, 160)
        self.set_decorated(False)
        self.set_keep_above(True)
        self.move(100, 100)  # Posisi awal
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        
        btn_ls = Gtk.Button(label="📂 List Files")
        btn_ls.connect("clicked", self.run_ls)

        btn_ping = Gtk.Button(label="🌐 Ping Google")
        btn_ping.connect("clicked", self.run_ping)

        btn_exit = Gtk.Button(label="❌ Tutup Menu")
        btn_exit.connect("clicked", lambda w: Gtk.main_quit())

        box.pack_start(btn_ls, True, True, 0)
        box.pack_start(btn_ping, True, True, 0)
        box.pack_start(btn_exit, True, True, 0)
        
        self.add(box)
        self.show_all()
    
    def run_ls(self, widget):
        subprocess.run(["ls", "-l"], text=True)
    
    def run_ping(self, widget):
        subprocess.run(["ping", "-c", "4", "google.com"], text=True)

win = FloatingMenu()
Gtk.main()