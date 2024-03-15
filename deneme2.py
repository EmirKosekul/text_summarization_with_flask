from transformers import pipeline

# pipeline oluştur
pipe = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")

# metin girdisi
input_text = "Space is a deep mystery that triggers humanity's endless curiosity and desire for exploration. The infinite void filled with stars, dazzling galaxies, and intriguing planets presents a landscape that challenges human imagination. Space exploration, aided by technological advancements, is offering increasingly more discoveries and insights. While clues to the existence of extraterrestrial life are being sought, space travel is expanding the boundaries of humanity. Black holes, interstellar dust clouds, and exoplanetary atmospheres found within the depths of space are among the topics that excite and intrigue scientists. Space provides an infinite realm for both science and human imagination to explore the limitless potential."
input_text2="Space is an infinite realm that has always captivated humanity's curiosity and imagination. Filled with stars, planets, galaxies, and many other mysterious phenomena, space serves as an endless frontier for exploration. Throughout history, humanity's interest in space has evolved, deepening with technological advancements. Space encompasses a vast universe expanding on a dizzying scale. With modern observatories and space exploration tools, scientists can peer beyond planets and stars. However, the boundaries of these discoveries remain unclear, often leading to more questions than answers. One of space's most striking features is its abundance of star systems. Our Solar System, home to nine planets including Earth, asteroids, comets, and other celestial bodies, holds potential candidates for life. Discoveries like evidence of water on Mars suggest that it might have once harbored conditions suitable for life. Additionally, Jupiter's moon Europa may host a vast ocean beneath its icy surface. Such findings are crucial for understanding humanity's place in the universe and the possibility of other life forms.Beyond our Solar System lie thousands of galaxies, stars, and planets. Structures like the Milky Way Galaxy contain billions of stars and their orbiting planets. Instruments like the Hubble Space Telescope capture images of distant galaxies, providing clues about the universe's expansion and evolution. They also enable the study of enigmatic phenomena such as supermassive black holes. Space exploration has pushed the boundaries of human technological and scientific capabilities, leading to innovative discoveries. Space agencies work on ambitious projects like sending humans to Mars and developing space tourism. Progress in fields like artificial intelligence, robotics, and space mining holds potential benefits not only for space exploration but also for improving life on Earth. However, space exploration is not just a technological adventure but also an exploration of humanity's existential and philosophical questions. It reflects humanity's efforts to understand itself and the universe. This journey of discovery deepens humanity's understanding of its nature, origins, and place in the cosmos. In conclusion, space serves as both a scientific laboratory and an endless frontier for humanity. Future discoveries will continue to unravel the mysteries of the universe. Space exploration expands not only humanity's technological limits but also its imagination and curiosity, making it an integral part of the human experience."
# modeli kullanarak soru oluştur
# Eğer sadece bir tane soru üretmek istiyorsanız, "num_return_sequences" parametresini 1 olarak ayarlayabilirsiniz.
generated_questions = pipe(input_text2, max_length=50, num_return_sequences=5, num_beams=5, early_stopping=True)
question=generated_questions[0]

#print(question)

# Oluşturulan soruları yazdır
for i, question in enumerate(generated_questions):
    print(f"Soru {i+1}: {question['generated_text']}")
