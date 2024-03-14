from transformers import pipeline

# pipeline oluştur
pipe = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")

# metin girdisi
input_text = "Space is a deep mystery that triggers humanity's endless curiosity and desire for exploration. The infinite void filled with stars, dazzling galaxies, and intriguing planets presents a landscape that challenges human imagination. Space exploration, aided by technological advancements, is offering increasingly more discoveries and insights. While clues to the existence of extraterrestrial life are being sought, space travel is expanding the boundaries of humanity. Black holes, interstellar dust clouds, and exoplanetary atmospheres found within the depths of space are among the topics that excite and intrigue scientists. Space provides an infinite realm for both science and human imagination to explore the limitless potential."

# modeli kullanarak soru oluştur
# Eğer sadece bir tane soru üretmek istiyorsanız, "num_return_sequences" parametresini 1 olarak ayarlayabilirsiniz.
generated_questions = pipe(input_text, max_length=50, num_return_sequences=1, num_beams=5, early_stopping=True)


# Oluşturulan soruları yazdır
for i, question in enumerate(generated_questions):
    print(f"Soru {i+1}: {question['generated_text']}")
