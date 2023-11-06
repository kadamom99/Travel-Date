import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar  # Import the Calendar widget
import datetime


# Function to calculate the end date of the trip based on the selected duration
def calculate_end_date(start_date, trip_duration):
    end_date = start_date + datetime.timedelta(days=trip_duration)
    return end_date

# Function to generate a list of available booking dates including weekends
def generate_booking_dates(start_date, trip_duration):
    booking_dates = []
    current_date = start_date

    while trip_duration > 0:
        booking_dates.append(current_date.strftime('%Y-%m-%d'))
        trip_duration -= 1
        current_date += datetime.timedelta(days=1)

    return booking_dates


# Function to handle the Generate button click event
def generate_dates():
    selected_date = calendar.get_date()
    trip_duration = int(days_spinbox.get())

    start_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
    end_date = calculate_end_date(start_date, trip_duration)
    booking_dates = generate_booking_dates(start_date, trip_duration)

    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Trip Start Date: {}\n".format(selected_date))
    result_text.insert(tk.END, "Trip End Date: {}\n".format(end_date.strftime('%Y-%m-%d')))
    result_text.insert(tk.END, "Available Booking Dates:\n")
    for date in booking_dates:
        result_text.insert(tk.END, "{}\n".format(date))
    result_text.config(state='disabled')


# Create the main application window
root = tk.Tk()
root.title("Travel Booking System")

# Create a Calendar widget using tkcalendar
calendar = Calendar(root, date_pattern="yyyy-mm-dd")
calendar.pack(padx=20, pady=10)

# Label and Spinbox for selecting the number of days
days_label = tk.Label(root, text="Select the number of days for the trip:")
days_label.pack(pady=5)
days_spinbox = tk.Spinbox(root, from_=1, to=30)
days_spinbox.pack(pady=5)

# Button to generate booking dates
generate_button = tk.Button(root, text="Generate", command=generate_dates)
generate_button.pack(pady=10)

# Text widget to display the result
result_text = tk.Text(root, height=10, width=30)
result_text.pack()

# Disable text widget so that users cannot edit it
result_text.config(state='disabled')

# Start the GUI main loop
root.mainloop()
