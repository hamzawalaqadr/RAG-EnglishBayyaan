import os
import whisper
from whisper.utils import get_writer

model = whisper.load_model('small')

def get_transcribe(audio: str, language: str = 'en'):
    return model.transcribe(audio=audio, language=language, verbose=True)

def save_file(results, format='tsv', output_folder='./output'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    writer = get_writer(format, output_folder)
    writer(results, f'transcribe.{format}')

def transcribe_multiple(files):
    for idx, file in enumerate(files):
        output_folder = f'./output{idx + 1}/'
        result = get_transcribe(audio=file)
        print('-'*50)
        print(f"Transcription for {file}:")
        print(result.get('text', ''))
        save_file(result, output_folder=output_folder)
        save_file(result, 'txt', output_folder=output_folder)
        save_file(result, 'srt', output_folder=output_folder)

audio_directory = './audio_files'
files = [os.path.join(audio_directory, f) for f in os.listdir(audio_directory) if f.endswith(('.mp3', '.wav'))]


transcribe_multiple(files)
