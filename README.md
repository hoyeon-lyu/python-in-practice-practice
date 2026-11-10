# Python in Practice 복습 예제

[shipthatcode Python in Practice](https://shipthatcode.com/courses/python-in-practice) 레슨을 공부한 뒤, 배운 내용을 확인하려고 푸는 복습 문제 모음입니다. 문제는 Claude가 출제하고, 풀이는 직접 작성합니다. 문제마다 입력/출력 테스트를 두고 스크립트로 채점합니다.

## 문제 목록
| # | 문제 | 다루는 개념 | 풀이 | 테스트 |
|---|---|---|---|---|
| 1 | [플레이리스트](problems/ex1.md) | `append`, `insert`, `pop(0)`, `remove`, `join` | [ex1.py](solutions/ex1.py) | |
| 2 | [센서 데이터 정리](problems/ex2.md) | 리스트 컴프리헨션, 조건식, `all` | [ex2.py](solutions/ex2.py) | |
| 3 | [곱셈표](problems/ex3.md) | 중첩 컴프리헨션, 2차원 리스트 | [ex3.py](solutions/ex3.py) | |
| 4 | [원점에서 가까운 순서](problems/ex4.md) | 튜플 정렬, 언패킹, `enumerate` | [ex4.py](solutions/ex4.py) | |

## 실행 방법
```sh
./run_tests.sh        # 전체 채점
./run_tests.sh ex2    # 예제 하나만
```
틀리면 실제 출력과 기대 출력의 차이(diff)를 보여줍니다. 테스트 하나당 2초 제한이 있어서, 무한 루프가 생기면 멈추고 `시간 초과`로 표시합니다.

## 폴더 구조
```
problems/   문제 설명
solutions/  내 풀이 (exN.py)
tests/      exN/1.in, 1.out … 입력과 기대 출력
run_tests.sh
```
