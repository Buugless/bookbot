def main():
    book_path="books/frankenstein.txt"
    text= get_book_text(book_path)
    number_words=count_words(book_path)
    #print("f{number_words} is the number of words in text" )
    characters=characters_count(book_path)
    #print(characters)
    converted=print_char_report(characters)
    #print(converted)
    print(f" ---Begin report of books/frankenstein.txt ---\n {number_words} words found in the document\n\n\n {converted}")
   
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
def count_words(text):
    count=0
    words=get_book_text(text)
    word_list=words.split()
    for i in range (0,len(word_list)):
        count=count+1
    return count
def characters_count(text):
    words=get_book_text(text)
    lowered_words=words.lower()
    characters_counted = {}
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in characters:
        count=0
        for j in lowered_words:
            if i == j:
                count=count+1
            else:
                pass
        characters_counted.update({i:count})
    return characters_counted
def print_char_report(dict):
    list_of_dicts = [{"char":k,"num":v} for k,v in dict.items()]
    def sort_by_count(item):
        return item["num"]
    list_of_dicts.sort(reverse=True,key=sort_by_count)
    report = ""
    for item in list_of_dicts:
        char=item["char"]
        count=item["num"]
        report+=(f"The '{char}' character was found {count} times\n")
    report += "---End report ---"
    return report
main()