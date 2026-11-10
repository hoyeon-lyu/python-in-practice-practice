# 예제 1. 플레이리스트
관련 레슨: 01 리스트 기초

첫 줄에 명령 개수 `n`, 이어서 명령 `n`줄을 받아 노래 목록(리스트)을 관리한다. 처음 목록은 비어 있다.
- `add 곡` → 목록 맨 뒤에 추가
- `first 곡` → 목록 맨 앞에 추가
- `next` → 맨 앞 곡을 목록에서 빼고 `play: 곡` 출력. 목록이 비어 있으면 `play: -`
- `drop 곡` → 그 곡을 목록에서 지운다(같은 곡이 여러 개면 맨 앞 하나만). 없으면 `not found: 곡`
- `list` → 목록을 `, `로 이어 한 줄로 출력. 비어 있으면 `(empty)`

| 입력 | 출력 |
|---|---|
| `7`<br>`add sky`<br>`add rain`<br>`first dawn`<br>`list`<br>`next`<br>`drop fog`<br>`list` | `dawn, sky, rain`<br>`play: dawn`<br>`not found: fog`<br>`sky, rain` |
| `6`<br>`next`<br>`list`<br>`add a`<br>`drop a`<br>`list`<br>`next` | `play: -`<br>`(empty)`<br>`(empty)`<br>`play: -` |

💡 맨 앞에 넣고 빼는 건 `insert(0, x)`와 `pop(0)`. 곡 이름에는 공백이 없다.
