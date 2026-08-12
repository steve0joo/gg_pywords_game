from pygame import mixer
import time
import csv

class WordGame:
    def __init__(self):
        self.WORD_FILE = 'data/word.txt'
        self.SCORE_FILE = 'word_game_score.csv'
        self.GOOD_SOUND = 'assets/good.wav'
        self.BAD_SOUND = 'assets/bad.wav'

        self.LIFE = 5           # 문제 출제 횟수
        self.PASS_SCORE = 3     # 합격 기준 정답 개수
        self.SOUND_DELAY = 1.0  # 효과음 재생을 기다리는 시간 (초)

    def playSound(self, sound_file):
        """효과음 파일을 재생하고 재생이 끝날 때까지 기다린다."""
        try:
            mixer.music.load(sound_file) # 소리파일 로딩
            mixer.music.play() # 소리 출력
            time.sleep(self.SOUND_DELAY)
        except Exception as err:
            print(f"예외가 발생했습니다. {err}")


    def loadWords(self, word_file):
        """단어 목록 파일을 읽어 한 줄에 한 단어씩 리스트로 반환한다."""
        try:
            with open(word_file, "r", encoding="utf8") as f:
                    return [word.strip() for word in f.readlines()]
        except FileNotFoundError as err:
            print(f"단어 목록 파일이 존재하지 않습니다. {err}")
        except Exception as e:
            print(f"예외가 발생했습니다. {e}")


    def askWord(self, trial, word):
        """문제를 화면에 출력하고 사용자의 답을 입력받는다."""
        action = input("\n준비? 엔터를 입력하세요. 종료하려면 'q'를 입력하세요.\n")
        if action == 'q':
            quit()
        print(f"Question #{trial + 1}\n")
        print(word)
        return input("")


    def wordLoad(self, answer, word):
        """입력한 답을 정답과 비교해 정답이면 1, 오답이면 0을 반환한다."""
        if(answer != word):
            print("못 맞춰서~")
            self.playSound(self.BAD_SOUND)
            return 0

        self.playSound(self.GOOD_SOUND)
        return 1


    def gameRun(self, words):
        """정해진 횟수만큼 문제를 출제하고 맞춘 개수를 반환한다."""
        correct = 0

        for trial in range(self.LIFE):
            answer = self.askWord(trial, words[trial])
            correct = correct + self.wordLoad(answer, words[trial])

        return correct


    def scorePrint(self, correct):
        """맞춘 개수를 기준으로 합격 여부를 출력한다."""
        if(correct >= self.PASS_SCORE):
            print("\n합격했습니다\n")
        else:
            print("\n불합격했습니다\n")


    def saveScore(self, score_file, execution_time, correct):
        """게임에 걸린 시간과 맞춘 개수를 CSV 파일로 저장한다."""
        header = ["게임 시간 (초)", "맞춘 개수"]
        data = [
            [f'{execution_time:.2f}', f'{correct}']
        ]

        with open(score_file, 'w', newline='', encoding='utf8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)


    def main(self):
        """단어 로딩부터 결과 저장까지 게임 전체 흐름을 실행한다."""
        mixer.init() # 초기화

        words = self.loadWords(self.WORD_FILE)

        start_time = time.perf_counter()
        correct = self.gameRun(words)
        execution_time = time.perf_counter() - start_time

        self.scorePrint(correct)
        print(f"게임 걸린시간: {execution_time:.2f} 초, 맞춘 개수 : {correct}개")

        self.saveScore(self.SCORE_FILE, execution_time, correct)


if __name__ == "__main__":
    wg = WordGame()
    wg.main()
