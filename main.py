from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint


def pdf2mp3(file_path='test.pdf', language='en'):
    print('Проверяем файлы')
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages)
            text = text.replace('\n', '')
            with open('text.txt', 'w') as file:
                file.write(text)
        print('Начинаем обработку аудиофайла....')
        audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        audio.save(f'{file_name}.mp3')
        return f'{file_name} was successfully saved!'
    else:
        return 'File not exist, check file path'


def main():
    tprint('PDF >>> 2 >>> MP3', font='block')
    file_path = input('Input pdf file path: ')
    file_language = input('Input a language, for ex "en" or "ru: ')
    print(pdf2mp3(file_path=file_path, language=file_language))


if __name__ == '__main__':
    main()
