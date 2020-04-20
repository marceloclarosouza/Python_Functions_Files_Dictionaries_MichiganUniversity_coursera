#Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.
emotion_words.txt 
Sad upset blue down melancholy somber bitter troubled
Angry mad enraged irate irritable wrathful outraged infuriated
Happy cheerful content elated joyous delighted lively glad
Confused disoriented puzzled perplexed dazed befuddled
Excited eager thrilled delighted
Scared afraid fearful panicked terrified petrified startled
Nervous anxious jittery jumpy tense uneasy apprehensive


emotion = open("emotion_words.txt", "r")
j_emotions = []
emo = emotion.readlines()

for line in emo:
    var = line.split()#split the text in lines

    for data in var:
        row = data.split()#split the lines in words

        for words in row:
            if words[0] == "j": #access the first char of each string
                j_emotions.append(words)
print(j_emotions)
emotion.close()