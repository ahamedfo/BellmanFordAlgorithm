import sys
from Solution import Solution

def read_file(filename):

    origin = 0
    incoming_edges = []
    outgoing_edges = []

    with open(filename, 'r') as input_file:

        origin = int(input_file.readline())
        string = input_file.readline()

        while not string == '':
            in_str = string.split()
            out_str = (input_file.readline()).split()

            incoming = {int(in_str[i]) : int(in_str[i+1]) for i in range(0, len(in_str), 2)}
            outgoing = {int(out_str[i]) : int(out_str[i+1]) for i in range(0, len(out_str), 2)}

            incoming_edges.append(incoming)
            outgoing_edges.append(outgoing)

            string = input_file.readline()
    return (origin, incoming_edges, outgoing_edges)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the testcase filepath as a command line argument")
    else:
        inp = read_file(sys.argv[1])
        sol = Solution(*inp).output()
        #print("Your Solution:")
        #print("============================================================================")
        print(sol)
        #print("============================================================================")
