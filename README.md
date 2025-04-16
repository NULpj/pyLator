# 🌐 pyLator - Python Translator

**pyLator** is a lightweight command-line translation tool using the power of Google Translate (via `deep-translator`).  
It allows users to list supported languages, translate between them, and get usage help — all from the terminal.

---

## 🚀 Features

- 🌍 View all available language codes
- ✍️ Translate typed or spoken text.
- 🛠️ Uses Google Translate through `deep-translator`.
- 🎤 Voice input using `speech_recognition`.
- 💡 Auto language detection supported!

---

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/NULpj/pyLator.git
cd pyLator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Usage

Simply run:

```bash
python main.py
```

You'll be prompted with a simple menu:

```
=== pyLator - Translator CLI ===
1. Show available languages
2. Translate text
3. Exit
4. Help
5. Credits
```

---

## 🌐 Language Codes

pyLator supports over 100 languages. Use option **1** in the menu to view all supported language codes (e.g., `en`, `fr`, `ja`, `ar`, `ko`, etc.)

---

## 📖 Example

Translate "Hello World" from English to France:

```
Enter the text to translate: Hello World
Source language (e.g., 'en' or 'auto'): en
Target language (e.g., 'fr'): fr

✅ Translation Result (en → fr):
=> Bonjour le monde
```

---

## Credits

- Created by: NULpj
- Translator: deep-translator (Google Translate wrapper)
- Voice Recognition: speech_recognition (Google Web Speech API)

---

## 📄 License

This project is licensed under the GNU License.
