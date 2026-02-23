import json
missing = object()

def tojson(value):
    if value is missing:
        return "<missing>"
    return json.dumps(value, separators=(",",":"), ensure_ascii=False)

def deep_diff(a, b, path="", out=None):
    if out is None:
        out = []

    if isinstance(a,dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            new_path = f"{path}.{k}" if path else k 
            av = a.get(k, missing)
            bv = b.get(k, missing)

            if av is missing or bv is missing:
                out.append((new_path, av, bv))
            else:
                deep_diff(av, bv, new_path, out)
        return out

    if a!=b:
        out.append((path, a, b))
    return out
A = json.loads(input())
B = json.loads(input())
diffs = deep_diff(A, B)
if not diffs:
    print("No differences")
else:
    diffs.sort(key=lambda x: x[0])
    for p, old, new in diffs:
        print(f"{p} : {tojson(old)} -> {tojson(new)}")
