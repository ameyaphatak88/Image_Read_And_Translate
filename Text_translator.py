from translate import Translator
translator = Translator(to_lang = "German")

def translate_to_text(str):
    translation = translator.translate(str)
    return translation