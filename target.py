import serial
import os

ser = serial.Serial('/dev/ttyACM0', 115200)

# Folder name
folder = "dataset"

os.makedirs(folder, exist_ok=True)

# Find next available filename
index = 1

while os.path.exists(f"{folder}/target_word{index}.txt"):
    index += 1

filename = f"{folder}/target_word{index}.txt"

# Send record command
ser.write(b'r')

data_started = False
samples = ""

while True:

    line = ser.readline().decode().strip()

    if line == "BEGIN_RAW":
        data_started = True
        continue

    if line == "END_DATA":
        break

    if data_started:
        samples += line

# Save file
with open(filename, "w") as f:
    f.write(samples)

print(f"Saved {filename}")