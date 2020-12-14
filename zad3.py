translation_dict = {
    "itself": "",
    "and": "also",
    "also": "and",
    "never": "almost never",
    "why": "for what reason" }

# zad3.1
file1 = open('/text/1930 FIFA World Cup.txt', 'r')
file2 = open('/text/2014 FIFA World Cup marketing.txt', 'r')
file3 = open('/text/Africa.txt', 'r')
file4 = open('/text/Ancient Egypt.txt', 'r')

files = [file1, file2, file3, file4]

for file in files:
    text = file.read()
    text = text.split()
    new_text=""
    for word in text:
        if word in translation_dict.keys():
            text.remove(word)
        else:
            new_text = new_text+word+' '
            
    print(new_text)
    file.close()
        
        
# zad3.2
file1 = open('/home/pi/Downloads/sport/1930 FIFA World Cup.txt', 'r')
file2 = open('/home/pi/Downloads/sport/2014 FIFA World Cup marketing.txt', 'r')
file3 = open('/home/pi/Downloads/sport/Africa.txt', 'r')
file4 = open('/home/pi/Downloads/sport/Ancient Egypt.txt', 'r')

files = [file1, file2, file3, file4]

for file in files:
    text = file.read()
    text = text.split()
    new_text2=""
    for index, word in enumerate(text):
        if word in translation_dict.keys():
            text[index] = translation_dict[word]
        new_text2 = new_text2+text[index]+' '
            
    print(new_text2)
    file.close()
    