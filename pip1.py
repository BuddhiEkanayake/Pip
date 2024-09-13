from transformers import pipeline



# Specify the model explicitly
classifier = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")
res = classifier("I've been waiting for a HuggingFace course my whole life.")
print(res)

