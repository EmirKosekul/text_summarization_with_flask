import random
from flask import Flask, jsonify, render_template, request

from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline("summarization", model="Falconsai/text_summarization")
question_generator = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")

main_text=""
result=""
header=""
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
    global result
    selected_text=""
    if request.method == 'POST':
        selected_text = request.form['gosterilenMetin']
        main_text=request.form['metinAlani']
        if request.form['action'] == 'first_action':
         header="Your summary is here!"
         result=summarizer(selected_text, max_length=1000, min_length=30, do_sample=False)[0]['summary_text']
        #  result=selected_text + " İlk işlem" 
        elif request.form['action'] == 'second_action':
         header="A question for you!"
         random_number = random.randint(1, 3)         
         generated_questions = question_generator(selected_text, max_length=50, num_return_sequences=5, num_beams=5, early_stopping=True)
         question=generated_questions[random_number]['generated_text']
         result=question
        #  result=selected_text + " İkinci işlem"    
        return render_template('rightclick.html', selected_text=selected_text,main_text=main_text ,result=result, header=header)
    return render_template('rightclick.html')

if __name__ == '__main__':
    app.run(debug=True)

# Space is a deep mystery that triggers humanity's endless curiosity and desire for exploration. The infinite void filled with stars, dazzling galaxies, and intriguing planets presents a landscape that challenges human imagination. Space exploration, aided by technological advancements, is offering increasingly more discoveries and insights. While clues to the existence of extraterrestrial life are being sought, space travel is expanding the boundaries of humanity. Black holes, interstellar dust clouds, and exoplanetary atmospheres found within the depths of space are among the topics that excite and intrigue scientists. Space provides an infinite realm for both science and human imagination to explore the limitless potential.