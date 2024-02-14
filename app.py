from flask import Flask, render_template, request

from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_text = request.form['input_text']
        summary = summarizer(input_text, max_length=1000, min_length=30, do_sample=False)[0]['summary_text']
        return render_template('index.html', input_text=input_text, summary=summary)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
