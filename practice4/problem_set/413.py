import json 
import sys
not_found = object()
def parse_query(q : str):
    tokens = []
    i = 0
    n = len(q)
    while i < n:
        if q[i] == '.':
            i += 1
            continue
        if q[i] == '[':
            j = q.find(']', i)
            if j == -1:
                return None
            idx_str = q[i+1:j]
            if not idx_str.isdigit():
                return None
            tokens.append(int(idx_str))
            i = j + 1
            continue
        j = i 
        while j < n and q[j] not in '.[':
            j += 1
        key = q[i:j]
        if key == "":
            return None
        tokens.append(key)
        i = j 
    return tokens
def resolve(data, tokens):
    cur = data 
    for t in tokens:
        if isinstance(t, str):
            if not isinstance(cur, dict) or t not in cur:
                return not_found
            cur = cur[t]
        else:
            if not isinstance(cur, list) or t < 0 or t >= len(cur):
                return not_found
            cur = cur[t]
    return cur                                                    
def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    try:
        data = json.loads(input_data[0])
    except:
        return
    try:
        q_count = int(input_data[1])
    except:
        return
    for k in range(q_count):
        query_str = input_data[2+k].strip()
        tokens = parse_query(query_str)
        if tokens is None:
            print("NOT_FOUND")
            continue
        ans = resolve(data,tokens)
        if ans is not_found:
            print("NOT_FOUND")
        else:
            print(json.dumps(ans, separators=(",",":"), ensure_ascii=False))
if __name__ == "__main__":
    main()                                                 