from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    try:
        # Create a Translator object
        translator = Translator()

        # Translate the text
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)

        return translated_text.text

    except Exception as e:
        return f"Translation error: {str(e)}"

def main():
    print("Language Translator")

    source_lang = input("Enter the source language (e.g., 'en' for English): ")
    target_lang = input("Enter the target language (e.g., 'es' for Spanish): ")
    text = input("Enter the text to translate: ")

    translated_text = translate_text(text, source_lang, target_lang)

    print(f"\nTranslated text: {translated_text}")

if __name__ == "__main__":
    main()                                                  