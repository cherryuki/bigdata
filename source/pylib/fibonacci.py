# -*- coding: utf-8 -*-
"""
피보나치 수열
"""
def fibo_print(n):
    "n미만의 피보나치 수열 print"
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
def fibo_return(n):
    "n미만의 피보나치 수열의 list를 return"
    result=[]
    a, b = 1, 1
    while a < n :
        result.append(a)
        a, b = b, a+b
    return result

# python fibonacci.py 200
# sys.argv : 명령행 인수

if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        fibo_print(int(sys.argv[1]))
    else:
        fibo_print(200)