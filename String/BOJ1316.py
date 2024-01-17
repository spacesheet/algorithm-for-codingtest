def group_word_checker(word):
    for j in range(0, len(word)-1):
        if word[j] != word[j + 1] and word[j] in word[j + 1:]:
            return False
    return True

def main() : 
    N = int(input())
    words = [input() for _ in range(N)]

    cnt = N
    for i in range(N):
        word = words[i]
        if not group_word_checker(word):
            cnt -= 1

    print(cnt)

main()