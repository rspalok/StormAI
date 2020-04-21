from googletrans import Translator
from gtts import gTTS
import os
import playsound
import random
from VirtAsst import virtFeatures

def speak(input_text,lang='en'):
    tts=gTTS(text=input_text,lang=lang)
    filename = virtFeatures.resource_path('voice.mp3')
    tts.save(filename)
    playsound.playsound(filename,True)
    os.remove(filename)


def langTranslator(statement,dest):
    print("text to be translated it "+statement)
    print("dest :" +dest)
    destination_lang_code= getLangcode(dest)
    print("destination_lang_code"+destination_lang_code)
    translator = Translator()
    output = translator.translate(statement , dest=destination_lang_code)
    print(output)
    speak(output.text, destination_lang_code)
    return output.text



def getLangcode(dest):
    LANGUAGES = {
         'af' : 'Afrikaans',
         'sq' : 'Albanian',
         'ar' : 'Arabic',
         'hy' : 'Armenian',
         'bn' : 'Bengali',
         'ca' : 'Catalan',
         'zh' : 'Chinese',
         'hr' : 'Croatian',
         'cs' : 'Czech',
         'da' : 'Danish',
         'nl' : 'Dutch',
         'en' : 'English',
         'eo' : 'Esperanto',
         'fi' : 'Finnish',
         'fr' : 'French',
         'de' : 'German',
         'el' : 'Greek',
         'hi' : 'Hindi',
         'hu' : 'Hungarian',
         'is' : 'Icelandic',
         'id' : 'Indonesian',
         'it' : 'Italian',
         'ja' : 'Japanese',
         'km' : 'Khmer',
         'ko' : 'Korean',
         'la' : 'Latin',
         'lv' : 'Latvian',
         'mk' : 'Macedonian',
         'no' : 'Norwegian',
         'pl' : 'Polish',
         'pt' : 'Portuguese',
         'ro' : 'Romanian',
         'ru' : 'Russian',
         'sr' : 'Serbian',
         'si' : 'Sinhala',
         'sk' : 'Slovak',
         'es' : 'Spanish',
         'sw' : 'Swahili',
         'sv' : 'Swedish',
         'ta' : 'Tamil',
         'th' : 'Thai',
         'tr' : 'Turkish',
         'uk' : 'Ukrainian',
         'vi' : 'Vietnamese',
         'cy' : 'Welsh'
    }
    try:
        key_list = list(LANGUAGES.keys())
        val_list = list(LANGUAGES.values())
        return key_list[val_list.index(dest)]
    except :
        virtFeatures.speak("I couldn't find the language you mentioned..\n"
                       "please repeat the langauage you want me to translate in..")
        dest = virtFeatures.myCommand().lower()
        return getLangcode(dest)