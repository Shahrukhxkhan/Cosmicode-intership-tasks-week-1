# Task 5: Time Conversion from Seconds
def convert_seconds(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds

# Example usage
total_seconds = int(input("Enter time in seconds: "))
h, m, s = convert_seconds(total_seconds)
print(f"{h} hours, {m} minutes, {s} seconds")