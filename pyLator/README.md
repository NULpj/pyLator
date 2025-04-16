# 🌐 pyLator - Simple CLI Translator

**pyLator** is a lightweight command-line translation tool using the power of Google Translate (via `deep-translator`).  
It allows users to list supported languages, translate between them, and get usage help — all from the terminal.

---

## 🚀 Features

- 🌍 View all available language codes
- 🔁 Translate text between any two languages
- 🆘 Help section with usage instructions
- 🎓 Credits page to acknowledge contributors
- 💡 Auto language detection supported!

---

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pyLator.git
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
python pyLator.py
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

pyLator supports over 100 languages. Use option **1** in the menu to view all supported language codes (e.g., `en`, `id`, `fr`, `ja`, `ar`, etc.)

---

## 📖 Example

Translate "Halo dunia" from Indonesian to English:

```
Enter the text to translate: Halo dunia
Source language (e.g., 'id' or 'auto'): id
Target language (e.g., 'en'): en
```

---

## 🙌 Credits

- Developed by: [Your Name Here]
- Powered by: [`deep-translator`](https://pypi.org/project/deep-translator/)
- Translation engine: Google Translate API (via wrapper)

---

## 📄 License

This project is licensed under the MIT License.
