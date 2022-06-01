import os

files = os.listdir(".")

reports = []
f = open('linker.js', 'w')

index = 0
for file in files:
    if(file.endswith(".json")):
        f.write("import file" + str(index) + " from './" + file + "'\n")
        reports.append(file)
        index+=1

f.write("const files=[\n")
for i in range(index):
    f.write("file"+str(i)+",\n")

f.write("];\n")
f.write("export {files};")
print("Done")
f.close()
