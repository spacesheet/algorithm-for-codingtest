def group_word_checker(word : str) -> bool :
    word_set = set()
    before = word[0]
    word_set.add(before)
    
    for w in range(1, len(word)) :
        if word[w] not in word_set :
            word_set.add(word[w])
            
            before = word[w]
            continue
        
        if before != word[w] :
            return False
        
        before = word[w]
        
    return True 

def main() : 
    N = int(input())
    result = 0
    for _ in range(N) :
        if group_word_checker(input()) :
            result += 1
    print(result)

main()