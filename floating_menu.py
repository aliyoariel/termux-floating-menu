import tkinter as tk

class FloatingMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Floating Menu")
        self.root.geometry("200x150")  
        self.root.attributes('-topmost', True)  # Tetap di atas aplikasi lain
        self.root.overrideredirect(True)  # Hilangkan border window

        # Buat frame utama
        frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # Tambahkan tombol interaktif
        btn1 = tk.Button(frame, text="🔎 Cek Files", command=self.run_ls)
        btn2 = tk.Button(frame, text="🌐 Ping Google", command=self.run_ping)
        btnExit = tk.Button(frame, text="❌ Tutup", command=root.quit)

        btn1.pack(fill="x", pady=5)
        btn2.pack(fill="x", pady=5)
        btnExit.pack(fill="x", pady=5)

        # Tambahkan fungsi untuk geser jendela
        frame.bind("<ButtonPress-1>", self.start_move)
        frame.bind("<B1-Motion>", self.on_move)

    def run_ls(self):
        print("Menjalankan 'ls' untuk melihat file...")

    def run_ping(self):
        print("Menjalankan 'ping google.com' untuk cek koneksi...")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        self.root.geometry(f"+{event.x_root-self.x}+{event.y_root-self.y}")

# Jalankan aplikasi
root = tk.Tk()
app = FloatingMenu(root)
root.mainloop()