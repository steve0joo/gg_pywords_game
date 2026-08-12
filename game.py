from pygame import mixer
import time
import csv

mixer.init() # 초기화
# mixer.music.load('assets/good.wav') # 단어를 맞췄을 때의 소리파일 로딩
# mixer.music.play() # 소리 출력

start_time = time.perf_counter()
correct = 0;

def wordLoad(answer, trial):
        if(answer != words[trial]):
            print("못 맞춰서~")
            mixer.music.load('assets/bad.wav') # 단어를 맞췄을 때의 소리파일 로딩
            mixer.music.play() # 소리 출력
            time.sleep(1.0) 
            return 0
        return 1

def gameRun():
    life = 5
    trial = 1
    correct = 0

    while (life > 0):
        print("\n준비? 엔터를 입력하세요.\n")
        print(f"Question #{trial}\n")
        print(words[trial])
        answer = input("")

        correct = correct + wordLoad(answer, trial)

        mixer.music.load('assets/good.wav') # 단어를 맞췄을 때의 소리파일 로딩
        mixer.music.play() # 소리 출력
        time.sleep(1.0) 

        life = life - 1
        trial = trial + 1

    return correct

def scorePrint(correct):
     if(correct >= 3):
        print("\n합격했습니다\n")
     else:
        print("\n불합격했습니다\n")



with open("data/word.txt", "r", encoding="utf8") as f:
    words = []
    read_words = f.readlines()

    for word in read_words:
        word = word.strip()
        words.append(word)

    print(words)

    correct = gameRun()

end_time = time.perf_counter()
execution_time = end_time - start_time

scorePrint(correct)

print(f"게임 걸린시간: {execution_time:.2f} 초, 맞춘 개수 : {correct}개")

header = ["게임 시간 (초)", "맞춘 개수"]
data = [
    [f'{execution_time:.2f}', f'{correct}']
]

with open('word_game_socre.csv', 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)