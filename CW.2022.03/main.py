from ui.window_main import MainWindow
from data.seed import Seed

# Populate data.
Seed().populate()

# Run application.
app = MainWindow()

x = y = 0

width = app.winfo_screenwidth()
height = app.winfo_screenheight()

app.geometry(f"{width}x{height}+{x}+{y}")
app.title("Email Manager")

app.mainloop()
