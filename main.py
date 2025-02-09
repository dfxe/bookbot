def count_characters(text:str):
    cc = [0] * len(string.ascii_lowercase)
    cc_list = list(string.ascii_lowercase)
    next_dict = {}
    for i,j in zip(cc_list, cc):
        next_dict[i]=j

    for char in text:
        if char.isalpha():
            next_dict[char.lower()] += 1
    return next_dict

if __name__ == '__main__':
    import string
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(count_characters(file_contents))

