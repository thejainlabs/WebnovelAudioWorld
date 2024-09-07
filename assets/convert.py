import os
from pydub import AudioSegment

# Define the directory containing the .m4a files
directory = 'suprememagus'  # Replace with the path to your folder

# Loop over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.m4a'):
        # Load the .m4a file
        m4a_path = os.path.join(directory, filename)
        audio = AudioSegment.from_file(m4a_path, format='m4a')

        # Define the output file path with .mp3 extension
        mp3_path = os.path.join(directory, os.path.splitext(filename)[0] + '.mp3')

        # Export as .mp3
        audio.export(mp3_path, format='mp3')
        print(f"Converted: {filename} -> {os.path.basename(mp3_path)}")