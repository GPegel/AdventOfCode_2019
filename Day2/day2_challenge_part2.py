# GAP => Gravity Assist Program

def read_input():
    with open("day2_input") as f:
        global GAP
        GAP = list(map(int, f.readline().split(",")))

def run_GAP():
    opcode_id = 0
    number1 = 1
    number2 = 2
    result = 3
    opcode = GAP[opcode_id]

    while opcode != 99:

        if opcode == 1:
            GAP[GAP[result]] = (GAP[GAP[number1]] + GAP[GAP[number2]])

        elif opcode == 2:
            GAP[GAP[result]] = (GAP[GAP[number1]] * GAP[GAP[number2]])

        opcode_id += 4
        number1 += 4
        number2 += 4
        result += 4
        opcode = GAP[opcode_id]

    return GAP[0]

def calc_GAP():
    for noun in range(100):
        for verb in range(100):
            read_input()
            GAP[1] = noun
            GAP[2] = verb
            output = run_GAP()
            if output == 19690720:
                return noun * 100 + verb

if __name__ == "__main__":
    print(calc_GAP())