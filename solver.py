import itertools

def does_not_contain(letters, word_list):
    # black letters
    if not letters:
        return word_list
    remove_list = []
    for word in word_list:
        for letter in letters:
            if letter in word:
                remove_list.append(word)
    for remove_word in remove_list:
        try:
            word_list.remove(remove_word)
        except:
            #print("Already removed... (black character)" + remove_word)
            continue
    return word_list

def does_contain(letters, nums, word_list):
    # yellow letters
    if not letters:
        return word_list
    remove_list = []
    for word in word_list:
        for letter in letters:
            if letter not in word:
                remove_list.append(word)
    for word in word_list:
        for (letter, num) in zip(letters, nums):
            if word[int(num) - 1] is letter:
                remove_list.append(word) 
    for remove_word in remove_list:
        try:
            word_list.remove(remove_word)
        except:
            #print("Already removed... (yellow character)" + remove_word)
            continue
    return word_list

def contains_in_positions(letter_1, letter_2, letter_3, letter_4, letter_5, word_list):
    # green letters
    remove_list = []
    if letter_1 != '*':
        for word in word_list:
            if word[0] != letter_1:
                remove_list.append(word)
    if letter_2 != '*':
        for word in word_list:
            if word[1] != letter_2:
                remove_list.append(word)
    if letter_3 != '*':
        for word in word_list:
            if word[2] != letter_3:
                remove_list.append(word)
    if letter_4 != '*':
        for word in word_list:
            if word[3] != letter_4:
                remove_list.append(word)
    if letter_5 != '*':
        for word in word_list:
            if word[4] != letter_5:
                remove_list.append(word)
    for remove_word in remove_list:
        try:
            word_list.remove(remove_word)
        except:
            #print("Already removed... (green character)" + remove_word)
            continue
    return word_list

def main():
    with open('possible_words.txt') as f:
        # read list of possible words
        word_list = []
        word_list.append(f.read().split('\n'))
        word_list = word_list[0]
        # read black, yellow, and green characters
        l_not_contain = input("Enter letters not in the word (blacked out characters): ")
        l_does_contain = input("Enter letters that exist in the word (yellow characters): ")
        num_list = []
        if l_does_contain:
            for letter in l_does_contain:
                num = input("What position is the " + letter + " not in? ")
                num_list.append(num)
        l_contain_in_pos_1 = input("Enter letter that exists in position 1 or * if you do not know (green character): ")
        l_contain_in_pos_2 = input("Enter letter that exists in position 2 or * if you do not know (green character): ")
        l_contain_in_pos_3 = input("Enter letter that exists in position 3 or * if you do not know (green character): ")
        l_contain_in_pos_4 = input("Enter letter that exists in position 4 or * if you do not know (green character): ")
        l_contain_in_pos_5 = input("Enter letter that exists in position 5 or * if you do not know (green character): ")
        # compile word list based on input information
        word_list = does_not_contain(l_not_contain, word_list)
        word_list = does_contain(l_does_contain, num_list, word_list)
        word_list = contains_in_positions(l_contain_in_pos_1, l_contain_in_pos_2, l_contain_in_pos_3, l_contain_in_pos_4, l_contain_in_pos_5, word_list)
        # print possible words for user
        print("These are the possible remaining words:")
        print(word_list)

if __name__ == "__main__":
    main()
