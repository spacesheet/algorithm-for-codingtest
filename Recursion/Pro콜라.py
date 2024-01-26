import sys
sys.setrecursionlimit(10**6)

def solution(a, b, n):
    answer = 0
    for _ in range(n):
        if n < a:
            return 0
        else:
            answer = (n // a) * b
            return answer + solution(a, b, n % a + answer)
    return answer