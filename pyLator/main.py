import speech_recognition as sr
from deep_translator import GoogleTranslator

def list_languages():
    translator = GoogleTranslator(source='auto', target='en')
    langs = translator.get_supported_languages(as_dict=True)
    print("\n📜 Available Languages:\n")
    for lang, code in langs.items():
        print(f"{lang.capitalize():<20} => {code}")
    print("\nUse the code on the right when translating.")

def get_text_input():
    print("\n📝 Input Method:")
    print("1. Type text")
    print("2. Speak with microphone")
    print("3. Back")
    method = input("Choose input method (1/2/3): ")

    if method == '1':
        return input("\nEnter the text to translate: "), False
    elif method == '2':
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                lang = input("🗣 Language of your speech (e.g., 'id', 'en'): ").lower()
                print("🎙 Please speak...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                text = r.recognize_google(audio, language=f"{lang}-{lang.upper()}")
                print(f"✅ Recognized Speech: {text}")
                return text, True
        except sr.UnknownValueError:
            print("❌ Sorry, speech not recognized.")
        except sr.RequestError:
            print("❌ Could not request results from speech service.")
        except Exception as e:
            print("❌ Error:", e)
    elif method == '3':
        print("↩️ Returning to main menu...")
        return None, None
    else:
        print("⚠️ Invalid choice.")
    return None, False

def translate_text():
    text, from_speech = get_text_input()
    if text is None and from_speech is None:
        return  # user chose to go back
    if text is None:
        return  # invalid input or error in speech recognition

    if from_speech:
        source = input("Detected speech language (used as source): ").lower()
    else:
        source = input("Source language (e.g., 'en'): ").lower()

    target = input("Target language (e.g., 'fr'): ").lower()

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        print(f"\n✅ Translation Result ({source} → {target}):")
        print("=> " + translated)
    except Exception as e:
        print("❌ An error occurred:", e)

def show_help():
    print("\n💡 Help - How to Use pyLator")
    print("- Option 1: View available language codes (e.g., 'en' = English).")
    print("- Option 2: Translate text (you can type or speak).")
    print("  - Use 'auto' for automatic source language detection.")
    print("- Option 3: Exit the program.")
    print("- Option 4: See this help guide.")
    print("- Option 5: View credits and tools used.")
    

def show_credits():
    print("\n🎉 Credits")
    print("- Created by: NULpj")
    print("- GitHub or Contact: https://github.com/NULpj")
    print("- Translator Engine: deep-translator (Google Translate wrapper)")
    print("- Speech Recognition: speech_recognition (Google Web Speech API)")
    print("- Language codes: ISO 639-1 standard")
    print("- Thanks for using pyLator!")

def main():
    while True:
        print("\n=== pyLator - Translator CLI ===")
        print("1. Show available languages")
        print("2. Translate (Text / Voice)")
        print("3. Exit")
        print("4. Help")
        print("5. Credits")
        choice = input("Select an option: ")

        if choice == '1':
            list_languages()
        elif choice == '2':
            translate_text()
        elif choice == '4':
            show_help()
        elif choice == '5':
            show_credits()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
