from ui.window_main import MainWindow
from data.seed import Seed

# Populate data.
Seed().populate()

# Run application.
app = MainWindow()

app.title("Email Manager")
app.attributes("-zoomed", True)

app.mainloop()
