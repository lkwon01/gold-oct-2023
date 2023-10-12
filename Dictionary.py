"""
Your module description
"""

sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True: 
    
    word = input('Enter a word in English or type "EXIT" to exit: ')
    if word.upper() == "EXIT":
        break
    elif word in sample_dict:
        print('Translation:', sample_dict[word])
    else:
        print("No match")
        
print('Bye!')
