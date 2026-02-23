import importlib

q = int(input())

queries = [input().split() for _ in range(q)]

results = []


for module_path, attr in queries:
    try:
        module = importlib.import_module(module_path)
    except Exception:
        results.append("MODULE_NOT_FOUND")
        continue

    if not hasattr(module, attr):
        results.append("ATTRIBUTE_NOT_FOUND")
        continue

    value = getattr(module, attr)
    results.append("CALLABLE" if callable(value) else "VALUE")

print("\n".join(results))