import sys

def find_sum(N, num_arr):
    ret = 0
    flags = [False]*N # do not use index 0
    #flag = 0
    for val in num_arr:
        num_iter = N/val
        if num_iter*val == N:
            num_iter -= 1
        for i in range(1,num_iter+1):
            if flags[val*i] == False:
                ret += val*i
                flags[val*i] = True
    return ret

# this solution overcounts
def find_sum_bruteforce(N, num_arr):
    ret = 0
    for num in range(N):
        for val in num_arr:
            if num % val == 0:
                ret += num
    return ret

if __name__ == "__main__":
    num_arr = [3,5]
    N = int(sys.argv[1])
    print find_sum(N, num_arr)
    #find_sum_bruteforce(N, num_arr)



