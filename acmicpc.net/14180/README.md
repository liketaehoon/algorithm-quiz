## 문제
길이가 N인 정수 배열 A가 주어진다. 배열의 특징 C는 ΣAi·i (1 ≤ i ≤ n) 으로
정의된다.

배열에서 수 하나를 고른 다음, 아무 위치로 이동시킬 수 있다. 이 때, 배열의
시작이나 끝으로도 옮길 수 있으며, 원래 위치로도 옮길 수 있다.

배열 A에서 수를 하나만 이동시켰을 때, 배열의 특징 C의 최대값을 구하는
프로그램을 작성하시오.

## 입력
첫째 줄에 N (2 ≤ N ≤ 200,000)이 주어진다.

둘째 줄에는 Ai (|Ai| ≤ 1,000,000)가 주어진다.

## 출력
배열에서 수를 하나만 움직인 후의 C의 최대값을 출력한다.

### 예제 입력
4
4 3 2 5

### 예제 출력
39

### 예제2 입력
5
1 1 2 7 1

### 예제2 출력
49

## 출처
[백준 Online Judge 14180번:배열의 특징](https://www.acmicpc.net/problem/14180)