with open("../demofile.txt", "a") as f:
    f.write("Cats make great private detectives.\n")
    f.write("Many historical figures loved cats.\n")
with open("../demofile.txt") as f:
    print(f.read())    

   