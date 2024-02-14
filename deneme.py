from transformers import pipeline
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

ARTICLE = """ 
Space is an endless mystery that fuels humanity's curiosity and desire for exploration. 
Beyond infinity, hidden in the interstellar voids, are galaxies, stars, and planets that 
challenge the human imagination. Space is a timeless arena; stars and celestial bodies 
silently dance within the universe for billions of years, dwarfing humanity's fleeting 
existence in comparison. Space triggers the quest of science while providing a platform 
for humanity to delve into deep contemplation about its own existence. This boundless 
void is filled with unknowns and harbors countless mysteries waiting to be discovered.
"""
print(summarizer(ARTICLE, max_length=1000, min_length=30, do_sample=False))
#>>> [{'summary_text': 'Hugging Face has emerged as a prominent and innovative force in NLP . From its inception to its role in democratizing AI, the company has left an indelible mark on the industry . The name "Hugging Face" was chosen to reflect the company\'s mission of making AI models more accessible and friendly to humans .'}]
