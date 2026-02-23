import json 
f = open("text.txt", "r")
data = json.load(f)
print("Interface Status")
print("=" * 80)
print(f"{'DN':60} {'Description':20} {'Speed':10} {'MTU':5}")
print("-" * 100)
for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]

    dn = attrs["dn"]
    descr = attrs["descr"]
    speed = attrs["speed"]
    mtu = attrs["mtu"]

    print(f"{dn:60} {descr:20} {speed:10} {mtu}")
f.close()    

