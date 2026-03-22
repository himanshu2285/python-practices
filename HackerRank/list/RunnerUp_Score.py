# Print runner up score of a game

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Remove duplicates
    unique_arr = list(set(arr))
    unique_arr.sort()
    
    # print runner up score
    print(unique_arr[-2])
    
    

# Sample Input 
# 5 
# 2 3 6 6 5

# Sample Output 
# 5