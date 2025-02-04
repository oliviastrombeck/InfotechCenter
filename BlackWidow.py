# Import necessary libraries
import sys  # sys module provides access to system-specific parameters and functions
import time  # time module allows time-related functions such as sleep

# Display a welcome message with developer's name
print("\nWelcome Branch - Developer: Olivia Strombeck")

# Display the software version message
print("\nWelcome to InfoTechCenter V1.0\n")

# Initialize variables
x = 0  # Variable for counting the loop iterations
ellipsis = 0  # Variable to control the number of periods in the loading message

# Loop to simulate system boot process
while x != 20:  # The loop will run 20 times, simulating the progress of booting
    x += 1  # Increment the loop counter by 1
    message = ("Infotech Center System Booting" + "." * ellipsis)  # Construct the message with growing ellipsis (periods)
    ellipsis += 1  # Increase the number of periods to be added to the message
    sys.stdout.write("\r" + message)  # Overwrite the current line with the new message (the \r returns the cursor to the start of the line)
    time.sleep(1)  # Wait for 1 second before continuing to the next iteration
    if ellipsis == 4:  # If we reach 4 periods, reset the counter
        ellipsis = 0  # Reset the ellipsis counter back to 0
    if x == 20:  # Once 20 iterations are completed
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")  # Display final success message after booting is completed
