from flask import Flask, jsonify, render_template, request

from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline("summarization", model="Falconsai/text_summarization")
main_text=""

@app.route('/orjinal', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form['input_text']
        summary = summarizer(input_text, max_length=1000, min_length=30, do_sample=False)[0]['summary_text']
        return render_template('summarize.html', input_text=input_text, summary=summary)
    return render_template('summarize.html')
@app.route('/', methods=['GET', 'POST'])
def index():
    global main_text
    selected_text=""
    if request.method == 'POST':
        selected_text = request.form['gosterilenMetin']
        main_text=request.form['metinAlani']
        summary=selected_text + " ben seçildim"
        return render_template('rightclick.html', selected_text=selected_text,main_text=main_text ,summary=summary)
    return render_template('rightclick.html')

if __name__ == '__main__':
    app.run(debug=True)

# Space is a deep mystery that triggers humanity's endless curiosity and desire for exploration. The infinite void filled with stars, dazzling galaxies, and intriguing planets presents a landscape that challenges human imagination. Space exploration, aided by technological advancements, is offering increasingly more discoveries and insights. While clues to the existence of extraterrestrial life are being sought, space travel is expanding the boundaries of humanity. Black holes, interstellar dust clouds, and exoplanetary atmospheres found within the depths of space are among the topics that excite and intrigue scientists. Space provides an infinite realm for both science and human imagination to explore the limitless potential.