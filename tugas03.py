def counterKata(nama_file):
    word_count={}
    with open(nama_file, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word,0)+1

    return word_count
print(counterKata("buah.txt"))