import pyaudio
import wave
import threading
import time


# Function to record audio continuously with enhanced quality
def record_audio(filename, rate=44100, chunk_size=2048, bit_depth=pyaudio.paInt24):
    # Initialize the PyAudio object
    p = pyaudio.PyAudio()

    # Open the microphone stream for recording
    stream = p.open(format=bit_depth,   # Use 24-bit resolution for better quality
                    channels=1,         # Mono audio (1 channel)
                    rate=rate,          # Sample rate (48000 Hz is higher quality)
                    input=True,         # Input stream (microphone)
                    frames_per_buffer=chunk_size)  # Larger chunk size for better quality

    print("Press Enter to start recording...")

    # Wait for the user to press Enter to start recording
    input()

    print("Recording audio...\nPress Enter to stop.")

    frames = []  # List to store audio data frames

    # Function to listen for Enter key press to stop recording
    def listen_for_enter():
        input()  # Wait for the Enter key press to stop recording
        stop_event.set()

    # Start a thread to listen for the Enter key press to stop recording
    stop_event = threading.Event()
    listen_thread = threading.Thread(target=listen_for_enter)
    listen_thread.start()

    # Record audio until Enter is pressed
    while not stop_event.is_set():
        data = stream.read(chunk_size)
        frames.append(data)

    # Add a 2-second delay before stopping the recording and saving the file
    #print("Waiting 1 second before stopping the recording...")
    time.sleep(2)  # Delay for 2 seconds

    # Stop the audio stream and terminate PyAudio
    print("Recording stopped.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio data to a .wav file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono audio (1 channel)
        wf.setsampwidth(p.get_sample_size(bit_depth))  # 24-bit depth
        wf.setframerate(rate)  # Sample rate (48000 Hz)
        wf.writeframes(b''.join(frames))  # Write the collected frames to the file

    print(f"Audio saved to {filename}")

# Main function to generate the file name based on current date and time
def main():

    filename = r"D:\VS Code HTML,CSS & JavaScript\Capstone Project (Medical Chatbot)\app1\data\audio.wav"

    # Start recording audio with enhanced quality settings
    record_audio(filename)

if __name__ == "__main__":
    main()
