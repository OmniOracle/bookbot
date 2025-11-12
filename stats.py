def get_num_words(book):
    return len(book.split())
    
def text_chars(book):
    chars = {}
    text_lower = book.lower()
    for x in (text_lower):
        if x in chars:
            chars[x] += 1 
        else: 
            chars[x] = 1
    return chars

list_of_chars = []
def sort_on(items):
    return items["num"]

def sorted_chars(chars_text):
    for char in chars_text:
        if char.isalpha():
            list_of_chars.append(
                {
                "char":char,
                "num": chars_text[char]
                }
                )
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
    

