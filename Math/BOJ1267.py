N = int(input())

def rate_plan_y(time_list : list) -> int :
    rate = 0
    for time in time_list :
        rate += (time // 30 + 1) * 10
    return rate

def rate_plan_m(time_list : list) -> int :
    rate = 0
    for time in time_list :
        rate += (time // 60 + 1) * 15
    return rate

def main() :
    call_time = list(map(int, input().split()))
    y = rate_plan_y(call_time)
    m = rate_plan_m(call_time)
    if y < m :
        print('Y', end=' ')
        print(y)
    elif y > m :
        print('M', end=' ')
        print(m)
    else :
        print("Y M", end=' ')
        print(y)

main()
    