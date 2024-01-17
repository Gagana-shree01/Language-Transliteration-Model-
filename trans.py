# import the module
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
#from translate import Translator
from googletrans import Translator

def process(inp,lang):
    print("sanscript.KANNADA==",sanscript.DEVANAGARI)
    print("lang==",lang)
    #print("sanscript.lang==",sanscript.lang)
    
    

    # the text to be transliterated
    #text = "nivu hegiddiri, illi ba"

    # printing the transliterated text


    converted_text=transliterate(inp, sanscript.ITRANS, lang)
    
    print("Coverted text==",converted_text)
    if lang=='devanagari':
        lang="hindi"
    else:
        lang=lang

    translator = Translator()
    res = translator.translate(converted_text)
    translation=res.text
    #print (translation
    print("English Translation",translation)
    return converted_text,translation

