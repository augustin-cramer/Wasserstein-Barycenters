from tqdm import tqdm
import time

def custom_bar_format(current_progress, total_length=30):
    rails = "__" * total_length
    train_position = min(current_progress, total_length - 1)
    train = rails[len(rails) // total_length * (train_position + 1):] + "🚂" + "🚃" * train_position
    return f"{current_progress/total_length*100:.0f}% {train} "

# Create a range of values for demonstration purposes
values = range(30)

# Create a tqdm instance with the custom bar format
progress_bar = tqdm(total=len(values), bar_format='{desc}')

# Iterate through the values
for value in values:
    # Update the description and advance the progress bar
    progress_bar.set_description(custom_bar_format(value))
    progress_bar.update(1)

    # Simulate some taskx
    time.sleep(0.2)
    
progress_bar.set_description(custom_bar_format(value))

# Close the progress bar
progress_bar.close()

print("Task completed!")