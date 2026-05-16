import serial
import os

# Arduino serial port
ser = serial.Serial('/dev/ttyACM0', 115200)

# Word label
word = "yes"

# Folder path
folder = f"dataset/{word}"

os.makedirs(folder, exist_ok=True)

# Find next filename
index = 1

while os.path.exists(f"{folder}/{word}_{index}.txt"):
    index += 1

filename = f"{folder}/{word}_{index}.txt"

# Start recording
ser.write(b'r')

data_started = False
samples = ""

while True:

    line = ser.readline().decode().strip()

    if line == "BEGIN_RAW":
        data_started = True
        print("Recording...")
        continue

    if line == "END_DATA":
        break

    if data_started:
        samples += line

# Save file
with open(filename, "w") as f:
    f.write(samples)

print(f"Saved {filename}")