def function_KR4(S):
    S += S
    n = len(S)
    sdvigi = [S[i:i+n//2] for i in range(n//2)]
    return min(sdvigi)

S = input().strip()
print(function_KR4(S))
