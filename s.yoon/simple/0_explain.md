# 간단한 문제들

## 숫자에 콤마 넣기

학원에서 했던 간단한 문제인데, 살짝 업그레이드 기능이 첨부된 형태  
문자열화된 숫자를 받는 것이니 리스트로 하나 씩 찢은다음 나머지가 2(즉 각 3번째)인 `0`을 `,0`으로 바꾸고 뒤집고 다시 문자열로 합쳐서 리턴
끝 숫자(즉 뒤집었을 때 첫번째 숫자)는 변경하지 않는 예외 조건을 걸어준다.

-와 소숫점은 각 `-`와 `.`가 있는지 체크하고 그 부분을 떼어내고 위의 로직을 처리하고, 마지막에 다시 붙여준다.

---

## 약수 구하기

루트N을 기점으로, 나머지가 0인 리스트를 구해서, 루트N이하의 약수로 N을 나눈 집합을 합친다.  
제곱수가 존재할경우 중복제거하는 로직은, 집합함수와 직접 찾는것 둘 다 경우에 따라 프로세스 타임이 다르지만 큰 차이는 없다.

---