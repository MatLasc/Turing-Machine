states = set()
input_alphabet = set()
tape_alphabet = []
transitions = {}


f = open("turing_machine", "r")

line = f.readline()
while line.strip() != "States:":
    line = f.readline()

line = f.readline()
while line.strip() != "Input alphabet:":
    states.add(line.strip())
    line = f.readline()

line = f.readline()
while line.strip() != "Tape alphabet:":
    input_alphabet.add(line.strip())
    line = f.readline()

line = f.readline()
while line.strip() != "Transitions:":
    tape_alphabet.append(line.strip())
    line = f.readline()

line = f.readline()
while line.strip() != "Start state:":
    line = line.strip()
    members = line.split(' ')
    source = members[0:3]
    dest = members[3:]
    transitions[tuple(source)] = dest
    line = f.readline()

start = f.readline().strip()

f.readline()

accept = f.readline().strip()

f.readline()

reject = f.readline().strip()

f.readline()
blank = f.readline().strip()


a = start
tape = [s for s in input()]
head1 = 0
head2 = len(tape) - 1
tape.append(blank)
while a != accept and a != reject:
    res = transitions[tuple([a, tape[head1], tape[head2]])]
    a = res[0]
    tape[head1] = res[1]
    tape[head2] = res[2]
    if res[3] == 'L':
        head1 -= 1
    else:
        if res[3] == 'R':
            head1 += 1
            if head1 == len(tape):
                tape.append(blank)
    if res[3] == 'L':
        head2 -= 1
    else:
        if res[3] == 'R':
            head2 += 1
            if head2 == len(tape):
                tape.append(blank)

if a == accept:
    print("Acceptat")
print(tape)