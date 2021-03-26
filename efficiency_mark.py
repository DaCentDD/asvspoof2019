import os
import statistics
import librosa
import sox
from concurrent.futures import ThreadPoolExecutor

directory = "flac"
lengths = []

for file in os.listdir(directory): 
    print(file)
    length = librosa.get_duration(filename=f"flac\\{file}")
    lengths.append(length)
    transform = sox.Transformer();
    transform.trim(length*0.25) 
    transform.build_file(f"flac\\{file}", f"75%\\{file}")
    lengths.append(librosa.get_duration(filename=f"75%\\{file}"))


with (open("median_length.txt", "a")) as info:
    info.writelines(f"100%: {statistics.median(lengths)}")






    

