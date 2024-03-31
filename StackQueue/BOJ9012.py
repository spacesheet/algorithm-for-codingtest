import sys
input = sys.stdin.readline

num = int(input())

def is_vps(ps : str) -> str:
    stack = []
    for i in ps :
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return 'NO'
    if not stack:
        return 'YES'
    else:
        return 'NO'
        
def main():
    for _ in range(num):
        print(is_vps(input()))

main()
