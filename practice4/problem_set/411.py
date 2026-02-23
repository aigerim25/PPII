import json 
def apply_patch(source, patch):
    if not isinstance(patch, dict) or not isinstance(source, dict):
        return patch
    for key, pval in patch.items():
        if pval is None:
            source.pop(key, None)
        else:
            sval = source.get(key)
            if isinstance(sval,dict) and isinstance(pval, dict):
                source[key] = apply_patch(sval, pval)
            else:
                source[key] = pval
    return source
source = json.loads(input())
patch = json.loads(input())
result = apply_patch(source, patch)
print(json.dumps(result, separators=(",",":"), sort_keys = True))                            