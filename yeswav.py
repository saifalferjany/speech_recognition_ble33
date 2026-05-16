import os
import numpy as np
from scipy.io.wavfile import write

word = "yes"

input_folder = f"dataset/{word}"
output_folder = f"wav_dataset/{word}"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        txt_path = os.path.join(input_folder, filename)

        with open(txt_path, "r") as f:
            data = f.read()

        samples = np.array(
            [int(x) for x in data.split(",") if x.strip() != ""],
            dtype=np.int16
        )

        wav_filename = filename.replace(".txt", ".wav")
        wav_path = os.path.join(output_folder, wav_filename)

        write(wav_path, 16000, samples)

        print(f"Converted {txt_path} -> {wav_path}")