from pydub import AudioSegment
from pydub.silence import split_on_silence


def remove_silence(input_file, format, silence_threshold=-50, silence_duration=500):
    # Load the audio file
    audio = AudioSegment.from_file(input_file, format=format)

    # Split the audio into chunks based on silence
    chunks = split_on_silence(
        audio,
        min_silence_len=silence_duration,
        silence_thresh=silence_threshold
    )

    # Combine non-silent chunks
    output = AudioSegment.empty()
    for chunk in chunks:
        output += chunk

    # Export the output audio to a file
    output.export("out"+input_file, format=format)


# Provide the input and output file paths
input_file = "melobytes.mp3"
format = "mp3"

# Remove silence from the audio file
remove_silence(input_file, format)
