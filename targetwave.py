import numpy as np
from scipy.io.wavfile import write
import os

input_folder = "dataset"
output_folder = "wav_dataset"

os.makedirs(output_folder, exist_ok=True)

# Convert every txt file
for filename in os.listdir(input_folder):

    if filename.endswith(".txt"):

        txt_path = os.path.join(input_folder, filename)

        with open(txt_path, "r") as f:
            data = f.read()

        # Convert text numbers to int16 array
        samples = np.array(
            [int(x) for x in data.split(",") if x.strip() != ""],
            dtype=np.int16
        )

        wav_name = filename.replace(".txt", ".wav")
        wav_path = os.path.join(output_folder, wav_name)

        # Save WAV
        write(wav_path, 16000, samples)

        print(f"Converted {filename} -> {wav_name}")