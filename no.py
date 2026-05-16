import serial
import os

ser = serial.Serial('/dev/ttyACM0', 115200)

word = "no"

folder = f"dataset/{word}"

os.makedirs(folder, exist_ok=True)

index = 1

while os.path.exists(f"{folder}/{word}_{index}.txt"):
    index += 1

filename = f"{folder}/{word}_{index}.txt"

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

with open(filename, "w") as f:
    f.write(samples)

print(f"Saved {filename}")