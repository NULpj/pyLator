from deep_translator import GoogleTranslator

def list_languages():
    translator = GoogleTranslator(source='auto', target='en')
    langs = translator.get_supported_languages(as_dict=True)
    print("\n📜 Available Languages:\n")
    for lang, code in langs.items():
        print(f"{lang.capitalize():<20} => {code}")
    print("\nUse the code on the right when translating.")

def translate_text():
    text = input("\nEnter the text to translate: ")
    source = input("Source language (e.g., 'en): ")
    target = input("Target language (e.g., 'fr'): ")

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        print(f"\n✅ Translation Result ({source} → {target}):")
        print("=> " + translated)
    except Exception as e:
        print("❌ An error occurred:", e)

def show_help():
    print("\n💡 Help - How to Use pyLator")
    print("- Option 1: View available language codes (e.g., 'en' = English).")
    print("- Option 2: Enter text and language codes to translate.")
    print("  - Use 'auto' for automatic source language detection.")
    print("- Option 3: Exit the program.")
    print("- Option 4: See this help guide.")
    print("- Option 5: View credits and tools used.")

def show_credits():
    print("\n🎉 Credits")
    print("- Created by: NULpj")
    print("- GitHub or Contact: https://github.com/NULpj")
    print("- Translator Engine: deep-translator (Google Translate wrapper)")
    print("- Library used: https://pypi.org/project/deep-translator/")
    print("- Language codes: ISO 639-1 standard")
    print("- Thanks for using pyLator!")

def main():
    while True:
        print("\n=== pyLator - Translator CLI ===")
        print("1. Show available languages")
        print("2. Translate text")
        print("3. Exit")
        print("4. Help")
        print("5. Credits")
        choice = input("Select an option : ")

        if choice == '1':
            list_languages()
        elif choice == '2':
            translate_text()
        elif choice == '3':
            print("Goodbye!")
            break
        elif choice == '4':
            show_help()
        elif choice == '5':
            show_credits()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
