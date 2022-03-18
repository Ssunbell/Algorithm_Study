# 🔥 멀티캠퍼스 알고리즘 스터디 🔥

<img width = "70%" src="https://user-images.githubusercontent.com/97590480/156875708-2d6bee9b-ce5c-4bbc-875a-5d6d5d85e51e.gif">

## ❗ 어떤 스터디인가요?

저희는 IT기업 입사에 필요한 코딩 테스트를 파이썬 언어를 사용하여 우수한 성적으로 통과하기 위해 학습하고 의견을 나누는 알고리즘 스터디입니다.
1. 코딩 테스트에 자주 나오는 개념에 대한 학습 및 백준 or 프로그래머스의 문제들을 풀면서 익힙니다.
2. 어느정도 코딩 테스트에 필요한 내용들을 학습했다면, 기출문제 위주로 문제풀이를 진행합니다.
3. 기출도 다 풀어봤다면 백준 기준 실버 ~ 골드 문제들을 선별하여 풀어봅니다.

## ❗ 어떤 식으로 진행되나요?

1. 1주일에 풀 문제를 선정하여 문제를 푼 뒤, 깃헙에 올립니다.
2. 매주 목요일 6시에 만나서 자신이 푼 문제에 대한 코딩 리뷰를 진행하고 피드백을 진행합니다.
3. 전날 12시까지(적어도 당일 점심까지) 레퍼지토리에 코드를 업로드해주셔야 합니다.

## ❗ 어떤 규칙을 지켜야 하나요?

### ✅ 파일 생성 및 업로드 규칙

1. 매주 새로운 디렉토리를 만듭니다. ex) 1주차, 2주차..
2. 디렉토리 안에 문제 디렉토리를 만듭니다. ex) 백준 1000번 문제라면 BOJ_1000
3. 문제 디렉토리 안에 각자 푼 문제를 `BOJ_1000_홍길동`의 형식으로 업로드합니다.
4. 최종적인 경로는 `1주차/BOJ_1000/BOJ_1000_홍길동` 입니다.

### ✅ 깃헙 Push/Pull 규칙

1. 무조건 __pull__ 먼저 해줍니다. pull을 해서 해당 주차의 디렉토리가 생기지 않는다면 따로 만들어주세요

```
$ git pull <remote 이름> <브랜치이름>
$ git pull AlgorithmStudy master
```

2. 파일 업로드 규칙에 맞게 push해주세요.
```
$ git add .
$ git commit -m "BOJ_1000_홍길동"
$ git push <remote 이름> master
```

3. 만일 내가 올린 코드에 수정/추가 등의 추가 커밋을 push할 경우에 커밋 형식을 다음과 같이 작성해주세요. 수정을 2번째 할 경우에 `fix2`를 붙여주시면 됩니다.

```
git commit -m "BOJ_1000_홍길동_fix"
git commit -m "BOJ_1000_홍길동_add"
```

## 📆 알고리즘 스터디 기록

### 🐱 백준

|날짜|개념|알고리즘 문제|문제번호|
|:---:|:---:|:---:|:---:|
|3.10|입출력|별 찍기, 문자열 반복, 크로아티아 알파벳, 팰린드롬, 크로스워드 만들기|BOJ_10995, BOJ_2675, BOJ_2941, BOJ_8892, BOJ_2804|
|3.17|list|나는 요리사다, 평균은 넘겠지, 나무 조각, 명령 프롬프트, 세로 읽기, 색종이, 직사각형 네 개의 합집합의 면적 구하기, 스도쿠 체점, 듣보잡, 다이얼, 나는야 포켓몬 마스터 이다솜, 2021 카카오 인턴 기출|BOJ_2804, BOJ_2953, BOJ_4344, BOJ_2947, BOJ_1032, BOJ_10798, BOJ_2563, BOJ_2669, BOJ_9291, BOJ_1764, BOJ_5622, BOJ_1620, PRO_KAKAO2021|
|3.24|재귀, 정렬, 브루트포스 알고리즘, 그리디 알고리즘|별 찍기 - 10, 나이순 정렬, 연구소, 에너지 드링크|BOJ_2447, BOJ_10814, BOJ_14502, BOJ_20115|
## 💖 참고사항

### 💕 원격 저장소 등록하기

`git remote add <원격저장소 이름> <주소>` 형식으로 작성합니다.

```bash
$ git remote add algorithmStudy https://github.com/Trailblazer-Yoo/Multicamp_Algorithm_Study.git
```

### 💕 원격 저장소 조회


`git remote -v`로 등록이 잘 됐는지 확인해봅니다.
```
$ git remote -v
algorithmStudy https://github.com/Trailblazer-Yoo/Multicamp_Algorithm_Study.git (fetch)
algorithmStudy https://github.com/Trailblazer-Yoo/Multicamp_Algorithm_Study.git (push)