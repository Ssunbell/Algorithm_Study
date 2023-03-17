"""
0.5초 -> 1000만
문자열 길이 5000 -> n^2 = 25,000,000 시간초과
"""
import sys
input = sys.stdin.readline

def hash_function(token): return ord(token)-96

def hashing(text):
    ans = 0
    for idx, token in enumerate(reversed(text)):
        ans += 27**idx * hash_function(token)
    return ans

def check(text, n):
    first_hash_value = hashing(text[:n])
    substrings = set()
    substrings.add(first_hash_value)
    for d, i in zip(text, text[n:]):
        first_hash_value -= 27**(n-1)*hash_function(d)
        first_hash_value *= 27
        first_hash_value += hash_function(i)
        if first_hash_value in substrings:
            return True
        substrings.add(first_hash_value)
    return False
    
def solve(text):
    txtlen = len(text)
    for sublen in range(txtlen-1, 0, -1):
        if check(text, sublen):
            return sublen

    return 0

if __name__ == "__main__":
    text = input().strip()
    print(solve(text))
