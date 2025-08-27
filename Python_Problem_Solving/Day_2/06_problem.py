#Digital Clock Simulation (Minutes Counter) ⏰

'''Print time in format HH:MM for 24 hours using loops.
Example: 00:00 → 23:59.
'''

for hour in range(24):       # Hours: 0 → 23
    for minute in range(60): # Minutes: 0 → 59
        print(f"{hour:02}:{minute:02}")