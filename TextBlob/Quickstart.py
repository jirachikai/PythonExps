from textblob import TextBlob
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print wiki.tags
print wiki.noun_phrases

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print testimonial.sentiment
print testimonial.sentiment.polarity