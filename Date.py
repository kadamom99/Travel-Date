import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime, timedelta

def calculate_travel_dates():
    selected_date = cal.get_date()
    num_days = int(num_days_var.get())
    start_date = datetime.strptime(selected_date, '%m/%d/%y').date()
    end_date = start_date + timedelta(days=num_days - 1)

    # Calculate available dates (including weekends) within the selected period
    available_dates = []
    current_date = start_date
    while current_date <= end_date:
        available_dates.append(current_date)
        current_date += timedelta(days=1)

    trip_start.config(text=f"Trip Start Date: {start_date.strftime('%Y-%m-%d')}")
    trip_end.config(text=f"Trip End Date: {end_date.strftime('%Y-%m-%d')}")
    available_dates_text.config(text=f"Available Dates:\n {[date.strftime('%Y-%m-%d') for date in available_dates]}")

# Create the main window
root = tk.Tk()
root.title("Travel Booking System")


# Calendar for selecting start date
cal = Calendar(root, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
cal.pack(padx=20, pady=10)

# Label and dropdown box for number of days
num_days_label = tk.Label(root, text="Select number of days:")
num_days_label.pack(padx=20, pady=10)
num_days_var = tk.StringVar()
num_days_dropdown = ttk.Combobox(root, textvariable=num_days_var, values=[i for i in range(1, 31)])
num_days_dropdown.pack(padx=20, pady=10)
num_days_dropdown.set(1)

# Button to calculate travel dates
calculate_button = tk.Button(root, text="Calculate Travel Dates", command=calculate_travel_dates)
calculate_button.pack(padx=20, pady=10)

# Labels to display calculated travel dates and available dates
trip_start = tk.Label(root, text="")
trip_start.pack(padx=20, pady=10)
trip_end = tk.Label(root, text="")
trip_end.pack(padx=20, pady=10)
available_dates_text = tk.Label(root, text="")
available_dates_text.pack(padx=20, pady=10)

# Run the GUI main loop
root.mainloop()

# # print("Text to speech is module for")

# this module is called as text to speech module and it used in siri and Goggle
# data class is not in the for while if elif else

# In
# a
# rule
# based
# solution, pronunciation
# solution is called as the encoding and used to guess what is the module used for the onehot encoding
# if the loop exists then the code will be execute separately
# Artifacts is  called as duplicate of same existing image and used for production


for i in range(10):
    print("program executed successfully...")


