import cv2
import pytesseract
from googletrans import Translator
import spacy
import nltk
from nltk.tokenize import word_tokenize
import numpy as np
import Levenshtein
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\aakas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Replace the file path below to an image that you want to read.
image = "airport1.jpeg"

# Load the image
img = cv2.imread(image)

# Preprocess the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray, 3)
cv2.imwrite("grey.jpeg", gray)

# Detect the text regions
config = '--psm 6 --oem 3 -l eng'
text = pytesseract.image_to_string(gray, config=config)

print("\n\nText Read : ", text)

# Cleaning and Processing the recognized text
nlp = spacy.load("en_core_web_md")
doc = nlp(text)


brown_corpus = nltk.corpus.brown.words()


text = ""

for token in doc:
    print(token.text,":",token.pos_)
    # Removing tokens with punctuation/symbol/interjection tags
    if(token.pos_ == "PUNCT" or token.pos_=="SYM" or token.pos_ == "SPACE" or token.pos_=="INTJ"):
        continue;
    else:
        # Appending proper nouns
        if(token.pos_=="PROPN" or (token.text==ent for ent in doc.ents)):
            text += str(token.text)+" "
            
        # Spell correction for other tags using brown corpus and levenshtein distance
        else:
            misspelled_word = str(token.text)
            distances = [(word, Levenshtein.distance(misspelled_word.lower(), word)) for word in brown_corpus]
            # Sort by distance
            distances.sort(key=lambda x: x[1])
            # Get closest word
            closest_word = str(distances[0][0])
            text+= closest_word+" "


# Replacing special characters with space
new_text = ""
for i in range(0,len(text)):
    if(text[i].isalnum()):
        new_text += str(text[i])
    else:
        new_text += " "        


text = new_text


# Tokenize the sentence into words
words = word_tokenize(text) 

# Remove non-alphabetic characters and convert to lowercase
words = [word.lower() for word in words if (word.isalnum() )] 

# Join the words back into a sentence
no_symbols = ' '.join(words) 
print("\n\nCleaned Text : ",no_symbols)


translator = Translator()


#TELUGU TRANSLATION
translated_text_telugu = translator.translate(no_symbols, src='en', dest='te').text

# Print the translated text
print("\nTranslated Text Telugu: ",translated_text_telugu)

# Generate an audio file of the translated text in Telugu using gTTS
tts = gTTS(translated_text_telugu, lang='te')
tts.save('translated_telugu.mp3')

# Play the audio file
os.system('start translated_telugu.mp3')


#MARATHI TRANSLATION
translated_text_marathi = translator.translate(no_symbols, src='en', dest='mr').text

# Print the translated text
print("\nTranslated Text Marathi: ",translated_text_marathi)

# Generate an audio file of the translated text in Marathi using gTTS
tts = gTTS(translated_text_marathi, lang='mr')
tts.save('translated_marathi.mp3')

# Play the audio file
os.system('start translated_marathi.mp3')



#HINDI TRANSLATION
translated_text_hindi = translator.translate(no_symbols, src='en', dest='hi').text

# Print the translated text
print("\nTranslated Text Hindi: ",translated_text_hindi)

# Generate an audio file of the translated text in Hindi using gTTS
tts = gTTS(translated_text_hindi, lang='hi')
tts.save('translated_hindi.mp3')

# Play the audio file
os.system('start translated_hindi.mp3')


#KANNADA TRANSLATION
translated_text_kannada = translator.translate(no_symbols, src='en', dest='kn').text

# Print the translated text
print("\nTranslated Text kannada: ",translated_text_kannada)

# Generate an audio file of the translated text in Kannada using gTTS
tts = gTTS(translated_text_kannada, lang='kn')
tts.save('translated_kannada.mp3')

# Play the audio file
os.system('start translated_kannada.mp3')


#TAMIL TRANSLATION
# Translate the text
translated_text_tamil = translator.translate(no_symbols, src='en', dest='ta').text

# Print the translated text
print("\nTranslated Text Tamil: ",translated_text_tamil)

# Generate an audio file of the translated text in Tamil using gTTS
tts = gTTS(translated_text_tamil, lang='ta')
tts.save('translated_tamil.mp3')

# Play the audio file
os.system('start translated_tamil.mp3')

