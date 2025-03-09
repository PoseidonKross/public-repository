import os
from pydub import AudioSegment

def analyze_file(file_path):
    try:
        if not os.path.exists(file_path):
            print("Error: File does not exist.")
            return
        
        if (ext := os.path.splitext(file_path)[1].lower()) not in ['.mp3', '.wav']:
            print("Error: Unsupported file format. Only mp3 and wav files are accepted.")
            return
        
        audio = AudioSegment.from_file(file_path)
        file_name = os.path.basename(file_path)
        file_length = len(audio) / 1000  # Length in seconds
        file_size = os.path.getsize(file_path) / (1024**2)  # Size in MB
        
        print(f"Name: {file_name}. Length is {file_length:.2f} seconds. Size is {file_size:.2f} MB.")
    
    except FileNotFoundError:
        print("Error: File not found.")
    except OSError as e:
        print(f"OS error: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    analyze_file('file.mp3')
