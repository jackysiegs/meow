with open('cat.txt', 'r') as cat:
              all_text = cat.read()
              real_text = str(all_text)
              data = real_text.split(",")

with open('dog.txt', 'r') as dog:
            all_text2 = dog.read()
            real_text2 = str(all_text2)
            data2 = real_text2.split(",")

ult = set(data) & set(data2)
print("Here are the macthing numbers from cat.txt and dog.txt\n")
print(ult)
