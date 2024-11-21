from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Define supported languages
LANGUAGES = {
    "English": "en",
    "Assamese": "as",
    "Bengali": "bn",
    "Sanskrit": "sa",
    "Gujarati": "gu",
    "Hindi": "hi",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Nepali": "ne",
    "Odia": "or",
    "Punjabi": "pa",
    "Tamil": "ta",
    "Telugu": "te",
    "Urdu": "ur",
    "Sindhi": "sd",
    "Bhojpuri": "bho",
    "Maithili": "mai",
    "Myanmar": "my",
    "Dogri": "doi",
}

@app.route("/", methods=["GET", "POST"])
def index():
    translations = {}
    input_text = ""
    selected_languages = []

    if request.method == "POST":
        input_text = request.form.get("text")
        selected_languages = request.form.getlist("languages")  # Get selected languages
        
        # If the "Translate" button is clicked, translate to the selected languages
        if selected_languages:
            for lang in selected_languages:
                code = LANGUAGES.get(lang)
                if code:
                    try:
                        # Translate using deep-translator
                        translated_text = GoogleTranslator(source='auto', target=code).translate(input_text)
                        translations[lang] = translated_text
                    except Exception as e:
                        translations[lang] = f"Error: {e}"

        # If the "Select All" button is clicked, select all languages and translate
        elif request.form.get("select_all"):
            selected_languages = list(LANGUAGES.keys())
            for lang in selected_languages:
                code = LANGUAGES.get(lang)
                if code:
                    try:
                        # Translate using deep-translator
                        translated_text = GoogleTranslator(source='auto', target=code).translate(input_text)
                        translations[lang] = translated_text
                    except Exception as e:
                        translations[lang] = f"Error: {e}"

    return render_template("index.html", input_text=input_text, translations=translations, languages=LANGUAGES, selected_languages=selected_languages)

if __name__ == "__main__":
    app.run(debug=True)
