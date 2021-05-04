import markovify

with open("corpus.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(1):
    print(text_model.make_sentence())

# 
# for i in range(3):
#     print(text_model.make_short_sentence(280))