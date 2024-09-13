from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# Specify the model explicitly
classifier = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")
res = classifier("I've been waiting for a HuggingFace course my whole life.")
print(res)

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english , tokenizer =tokenizer")
res = classifier("I've been waiting for a HuggingFace course my whole life.")
print(res)

sequence = "Using a transformer network is simple"
res= tokanizer(sequence)
print(res)

tokens = tokenizer.tokenize(sequence)
print(tokens)

decoded_string = tokenizer.decode(ids)
print(decoded_string)
