# GAP => Gravitiy Assist Program 
def read_GAP_data(file):
    with open(file) as f:
        return list(map(int, f.read().split(',')))

def run_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    pc = 0
    while pc < len(program):
        opcode = program[pc]
        op1 = program[program[pc + 1]]
        op2 = program[program[pc + 2]]
        dest = program[pc + 3]
        if opcode == 1 or opcode == 2:
            program[dest] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 99:
            break
        else:
            print('Encountering an unknown opcode!')
            break
    return program[0]

def output():
    return run_program(read_GAP_data('day2_input'), 12, 2)

print(output())