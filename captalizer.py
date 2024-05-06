lower_case_words = ["a", "an", "the", "at", "by", "for", "in", "of", "on", "to", "up", "and", "as", "but", "or", "nor"]

def capitalize_if(word):
    if not word in lower_case_words:
        return word.capitalize()
    else:
        return word

string = input(":")
split_string = string.split()
capped_string = [capitalize_if(word) for word in split_string]
print(" ".join(capped_string))