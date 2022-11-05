welcome = 'hello\nwelcome to word game'
print(welcome)
rules = 'rules:\nThe number of litter guesses is half of the word length\nThe number of guesses is one third\nThe minimum word length is three\nThe maximum word length is twenty'
print(rules)
while True:
    word = input("inter a word: ")
    len_word = len(word)
    hash_ = '_'
    hash_ *= len_word
    print('your chance',len_word // 2)
    print(hash_)
    
    chance = len_word // 2
    while True:
        
        litter = input('inter a litter: ')
        
        
        chance -= 1
        for j in word:
            if litter in j:
                index = [i for i,x in enumerate(word) if x == litter]
                for y in index:
                    hash_ = hash_[:y] + litter + hash_[y+1:]
                
        if litter not in word:
            
            print('no')  
        print('your chance',chance)     
        print(hash_)
        if chance == 0:
            print('end your chance')
            break
        elif hash_ == word:
            print('you inter word')
            break
    max_count = 3
    while True:
        
        guesses_word = input("inter you guesses word: ")
        max_count -= 1
        if guesses_word != word:
            print('your chance',max_count)
        if guesses_word == word:
            print("you won")
            break
        elif max_count == 0:
            print('you lose')
            break
    answer = input("do you continue(y/n): ")
    answer.lower()
    if answer == "n":
        print('good bye')
        break




