# KAKAO 2018년 신입공채 1차문제

문제 링크  
<http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/>

풀이는 전부 Python  
코드 링크 : <https://github.com/senel-study/kosmo-3rd/tree/master/s.yoon/KaKao>  
(_my : 내 코드, _answer : 인터넷에 있는 풀이 코드 )  

---
테스트 입력 값을 깔끔하게 넣는법

```python
result = [foo(s, c) for s, c in zip(obj1, obj2)]
```

zip함수를 사용하여 함수의 인수를 리스트순서대로 넣을 수 있고, 반복문으로 함수의 리턴값이 리스트에 이쁘게 들어간다.

---

1번 문제(비밀 지도)  
코딩도장 링크 : <http://codingdojang.com/scode/570>  

문제의 포인트는 2진수로 변환해서 하나라도 1이면 #으로 바꾸는 것, 비트연산자 `|`를 사용하는 것.  
(실제 문제에서는 if else를 사용해도 합격처리헀지만, 의도와 벗어난 방법)

새로 알게 된 기능  
`zfill(n)` : n의 자리만큼 0을 채워준다.(앞에서부터)  
`format(int, 'b')` : 2진수, 바이너리를 제거하고 출력해준다.  
`bin(a|b)` : 문제풀이의 핵심, 비트연산자 `|`를 넣으면 서로 자리값의 비트를 비교해서 어느쪽이든 1이 있으면 1이 나오게된다.

```python
>>> format(8|3, 'b').zfill(5)
'01011'
```

---

2번 문제(다트 게임)  
코딩도장 링크 : <http://http://codingdojang.com/scode/571>  

문자열 처리 문제, 숫자 1,10이 있는 경우를 해결하는 것이 포인트. 정규식을 사용하면 쉽게 나눌 수 있다.
`'\d{1,2}[SDT][*#]?'`가 이 다트식 한 점의 정규식.  
`re.findall(r'\d{1,2}[SDT][*#]?', str)`로 리스트에 넣어 관리할 수 있다.

싱글,더블,트리플(이 문제에선 제곱/세제곱이지만)의 계산식으로 if문을사용하지 않고 `'0SDT'.find(s[-1])`을 사용한 점이 라인수를 현저하게 줄일 수 있는 방법.

find()함수는 문자열에서 위치를 리턴해 주니까, 저 경우 S면 1, D면 2, T면 3을 리턴해줘서 조건문 없이 바로 연산에 사용할 수 있다.

---

3번 문제(캐시)
코딩도장 링크 : <http://codingdojang.com/scode/572>  

기사시험에 나오는 LRU알고리즘, 들어온지 가장 오래된 값을 캐시 페이지에서 지우는 알고리즘.  
리스트를 만들어서 새로운 것이 들어왔을때 인덱스0번을 지워버리고 새로운 값을 추가하면 된다.

문제의 포인트는 캐시크기가 0일 때인데, 예외처리를 수동으로 해주었는데, 코딩도장에서 본 방법으로 예외처리 없이 하나의 로직으로 대응이 가능했다.

제일 빨리 푼 문제.(떨어진 기사시험이 이걸...)

---

4번 문제 (보류)

---

5번 문제 (뉴스 클러스터)

포인트는 중복 허용집합, pyPI에서 multiset을 제공하는 것 같은데, 일단 알고리즘을 짜서 개인적으로 작성.
딱히 코드의 낭비는 없어 보인다.  

중복 집합이니 리스트로 넣고, 집합의 요소는 `set()`함수를 때려버리면 중복이 자동으로 제거되니까, 그걸로 갯수를 세서 교집합, 합집합을 만들어주면 됨.

합집합이 공집합일 경우만 예외로 제외하면 되니, 따로 조건분기 설정

---

6번문제(프렌즈4블록)

리스트를 쪼개서 좌표처럼 쓰면서 스캔, 인덱스 범위가 벗어나지 않게 반복문을 쓰는 것이 핵심. 특히 터진 다음 이동 처리가 결국 이동이 존재할 경우에 한 번 더 이동체크를 하는 건데 굉장히 비효율적으로 느껴지는데 다른 더 좋은 알고리즘이 있는지는 잘 모르겠음.

리스트 인덱스를 x,y값처럼 쓰는데 실제 수학적 위치와 달라서 반복문을 쓰는데 굉장히 고통.

처음에는 함수 자체를 재귀했는데, 그러면 리턴값을 글로벌 변수로 선언하지 않으면 에러가 나서 기능별로 객체화시키는 김에 반복 부분만 while로 감싸서 해결. 이쪽이 실행속도도 절반정도로 줄어드는 것 같다.