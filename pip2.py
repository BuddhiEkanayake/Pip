from transformers import pipeline

generator = pipeline("text-genareration", model="distilgpt")

res = generator(
    "In This Lesson ,we will teach you how to ",
    max_length=30,
    num_return_sequences=2,
)

print(res)