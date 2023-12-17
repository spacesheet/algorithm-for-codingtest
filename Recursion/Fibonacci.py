# 메모이제이션을 위한 딕셔너리 초기화
fibonacci_cache = {}

def fibonacci(n):
    # 메모이제이션: 이미 계산한 값이 있다면 반환
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # 피보나치 수열 계산
    if n <= 2:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    
    # 결과를 메모이제이션에 저장
    fibonacci_cache[n] = result
    return result

n = int(input())
print(f"피보나치 {n}번째 항: {fibonacci(n)}")