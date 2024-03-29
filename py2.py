import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the clock
clock_label = tk.Label(window, font=("Arial", 80), bg="black", fg="pink")
clock_label.pack(padx=0, pady=0)

# Start updating the clock
update_clock()

# Start the application main loop
window.mainloop()
