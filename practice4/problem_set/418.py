x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())
den = y1 + y2 
if abs(den) < 1e-12:
    x = x1 
else:
    t = y1 / den
    x = x1 + t*(x2-x1)
print(f"{x:.10f} {0.0:.10f}")         