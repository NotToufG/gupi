def median(lst):
    s=sorted(lst)
    n=len(s)
    m=n//2
    return (s[m-1]+s[m])/2 if n%2==0 else s[m]