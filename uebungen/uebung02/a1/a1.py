import sys
import time

regs = [0] * 100
instr = []
labels = {}

# Datei laden
f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip()
    if line == "" or line.startswith(";"):
        continue
    if line.startswith("LABEL"):
        parts = line.split()
        labels[parts[1]] = len(instr)
    else:
        instr.append(line)

regs[0] = int(sys.argv[2])

start = time.time()
pc = 0
while pc < len(instr):
    line = instr[pc]
    line = line.split(";")[0].strip()
    parts = line.replace(",", " ").split()
    op = parts[0]
    
    if op == "LOAD":
        r = int(parts[1][1:])
        regs[r] = int(parts[2])
    elif op == "ADD":
        r1 = int(parts[1][1:])
        if parts[2][0] == "R":
            r2 = int(parts[2][1:])
            regs[r1] = regs[r1] + regs[r2]
        elif parts[2][0] == "%":
            regs[r1] = regs[r1] + int(parts[2][1:])
    elif op == "SUB":
        r1 = int(parts[1][1:])
        r2 = int(parts[2][1:])
        r3 = int(parts[3][1:])
        regs[r1] = regs[r2] - regs[r3]
    elif op == "DEC":
        r = int(parts[1][1:])
        regs[r] = regs[r] - 1
    elif op == "JNZ":
        r = int(parts[1][1:])
        if regs[r] != 0:
            pc = labels[parts[2]]
            continue
    pc = pc + 1

end = time.time()
print("Summe von 0 bis", regs[0], ":", regs[2])
print("Laufzeit:", round(end - start, 6), "Sekunden")
