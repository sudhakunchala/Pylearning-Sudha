# reverse the sentence and every word should start with capital letter
# input= "india is my country"
# output= "Country My Is India"

def rev_words(sentence):
    words=sentence.split() # spliting sentence
    reverse_words=words[::-1] # it will reverse the words
    result= " ".join(reverse_words) # joining the words
    return result.title()  # capitalize first letter of each word

input_sentence="india is my country"
output_sentence= rev_words(input_sentence)
print(output_sentence)
