# gg_pywords_game

터미널에서 즐기는 영어 단어 받아쓰기 게임입니다. 화면에 보여준 단어를 그대로 입력해서 맞추면 되고, 정답 여부에 따라 효과음이 재생됩니다. 게임이 끝나면 소요 시간과 정답 개수를 CSV 파일로 저장합니다.

## 게임 규칙

- 총 5문제가 출제됩니다 (기회 5회).
- 화면에 단어가 표시되면 동일하게 입력한 뒤 엔터를 누릅니다.
- 정답이면 `good.wav`, 오답이면 `bad.wav` 효과음이 재생됩니다.
- **3개 이상** 맞추면 합격, 그렇지 않으면 불합격입니다.

## 요구 사항

- Python 3.12 이상
- [pygame](https://www.pygame.org/) 2.6.1 이상
- 효과음 재생을 위한 오디오 출력 장치

## 설치 및 실행

[uv](https://docs.astral.sh/uv/) 사용 (권장):

```bash
uv sync
uv run game.py
```

pip 사용:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install "pygame>=2.6.1"
python game.py
```

> 단어 목록과 효과음을 상대 경로(`data/`, `assets/`)로 읽기 때문에 **프로젝트 루트에서 실행**해야 합니다.

## 실행 예시

```
준비? 엔터를 입력하세요.

Question #1

number
number

...

합격했습니다

게임 걸린시간: 21.34 초, 맞춘 개수 : 4개
```

## 프로젝트 구조

```
gg_pywords_game/
├── game.py                 # 게임 본체
├── data/
│   └── word.txt            # 출제 단어 목록 (9,858개, 한 줄에 한 단어)
├── assets/
│   ├── good.wav            # 정답 효과음
│   └── bad.wav             # 오답 효과음
├── pyproject.toml          # 프로젝트 메타데이터 및 의존성
└── word_game_score.csv     # 실행 후 생성되는 결과 파일
```

### 주요 함수

| 함수 | 설명 |
| --- | --- |
| `wordLoad(answer, trial)` | 입력한 답과 정답을 비교해 정답이면 `1`, 오답이면 `0`을 반환 |
| `gameRun()` | 목숨이 소진될 때까지 문제를 출제하고 총 정답 개수를 반환 |
| `scorePrint(correct)` | 정답 개수를 기준으로 합격/불합격을 출력 |

## 결과 저장

게임이 끝나면 프로젝트 루트에 `word_game_score.csv`가 생성됩니다.

```csv
게임 시간 (초),맞춘 개수
21.34,4
```

실행할 때마다 덮어쓰기(`w` 모드)되므로 이전 기록은 남지 않습니다.

## 단어 목록 변경

`data/word.txt`의 각 줄이 하나의 문제로 사용됩니다. 원하는 단어 목록으로 파일을 교체하면 그대로 출제됩니다 (UTF-8 인코딩).
