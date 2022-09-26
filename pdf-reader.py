import json
import PyPDF2
from gtts import gTTS

config = open("./config.json")
json_config = json.load(config)
pdf_path = json_config["pdf_path"]
reading_speed = json_config["reading_speed"]
volume = json_config["volume"]
audio_file_name = json_config["audio_file_name"]

pdf_file_object = open(pdf_path, "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
pdf_text = ""

for page_num in range(pdf_reader.numPages):
    page_object = pdf_reader.getPage(page_num)
    pdf_text += page_object.extractText()
print(pdf_text)
pdf_file_object.close()

tts = gTTS(text=pdf_text, lang='en', tld='ca')
tts.save("audio_copy_of_pdf.mp3")