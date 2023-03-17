from math import gcd
def solution(numer1, denom1, numer2, denom2):
    numer3 = numer1 * denom2 + numer2 * denom1
    denom3 = denom1 * denom2
    
    num = gcd(numer3,denom3)
    
    answer = [numer3/num,denom3/num]
    return answer