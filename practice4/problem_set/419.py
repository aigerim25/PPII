import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

A = (x1, y1)
B = (x2, y2)

def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])

def dot(p, q):
    return p[0]*q[0] + p[1]*q[1]

def norm(p):
    return math.hypot(p[0], p[1])

def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def dist_to_segment_origin(A, B):
    ax, ay = A
    bx, by = B
    vx, vy = bx - ax, by - ay
    vv = vx*vx + vy*vy
    if vv == 0.0:
        return math.hypot(ax, ay)
    t = - (ax*vx + ay*vy) / vv
    t = clamp(t, 0.0, 1.0)
    px, py = ax + t*vx, ay + t*vy
    return math.hypot(px, py)

eps = 1e-12
if dist_to_segment_origin(A, B) >= R - eps:
    print(f"{dist(A, B):.10f}")
    raise SystemExit


rA = norm(A)
rB = norm(B)

tA = math.sqrt(max(0.0, rA*rA - R*R))
tB = math.sqrt(max(0.0, rB*rB - R*R))


cos_theta = clamp(dot(A, B) / (rA * rB), -1.0, 1.0)
theta = math.acos(cos_theta)


alpha = math.acos(clamp(R / rA, -1.0, 1.0))
beta  = math.acos(clamp(R / rB, -1.0, 1.0))


arc1 = max(0.0, theta - alpha - beta)
arc2 = max(0.0, 2.0*math.pi - theta - alpha - beta)
arc = min(arc1, arc2)

ans = tA + tB + R * arc
print(f"{ans:.10f}")