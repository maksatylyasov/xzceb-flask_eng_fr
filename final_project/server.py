from machinetranslation import translator
from machinetranslation.translator import englishToFrench,frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrenchFunction():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text=englishToFrench(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglishFunction():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text=frenchToEnglish(textToTranslate)
    return translated_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
