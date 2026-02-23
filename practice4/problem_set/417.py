import math 
R = float(input().strip())

x1 , y1 = map(float,input().split())
x2 , y2 = map(float, input().split())

dx = x2 - x1 
dy = y2 - y1 

a = dx*dx + dy*dy 
def out(val : float):
    print(f"{val:.10f}")
if a == 0.0:
    #inside = (x1*x1 + y1*y1) <= R*R + 1e-12
    out(0.0)
    raise SystemExit 
b = 2.0 * (x1*dx + y1*dy)
c = x1*x1 + y1*y1 - R*R    
disc = b*b - 4.0*a*c 
eps = 1e-12
if disc < -eps:
    out(0.0)
    raise SystemExit

if disc < 0.0:
    disc = 0.0 
sqrt_disc = math.sqrt(disc)
t1 = (-b - sqrt_disc) / (2.0 * a)
t2 = (-b + sqrt_disc) / (2.0 * a)
t_enter = min(t1,t2)
t_exit = max(t1,t2)
left = max(0.0, t_enter)
right = min(1.0, t_exit)
if right <= left:
    out(0.0)
else:
    seg_len = math.sqrt(a)
    out((right - left) * seg_len)      

