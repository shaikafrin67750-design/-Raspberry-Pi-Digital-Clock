# Raspberry Pi Digital Clock using Python

import tkinter as tk
from datetime import datetime

def update_clock():
current_time = datetime.now().strftime("%H:%M:%S")
current_date = datetime.now().strftime("%d-%m-%Y")

```
time_label.config(text=current_time)
date_label.config(text=current_date)

# Update every 1 second
root.after(1000, update_clock)
```

# Create window

root = tk.Tk()
root.title("Raspberry Pi Digital Clock")
root.geometry("600x300")

# Clock title

title_label = tk.Label(
root,
text="RASPBERRY PI DIGITAL CLOCK",
font=("Arial", 24)
)
title_label.pack(pady=20)

# Time display

time_label = tk.Label(
root,
text="00:00:00",
font=("Arial", 60)
)
time_label.pack()

# Date display

date_label = tk.Label(
root,
text="00-00-0000",
font=("Arial", 24)
)
date_label.pack(pady=10)

# Start clock

update_clock()

# Run application

root.mainloop()
