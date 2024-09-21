from fibonacci import test_start, calculate
from time import time_ns

def main():
    print("Press 1 for timed test, 2 for debug test (slightly slower) > ", end="")

    index = -1
    while index == -1:
        index = int(input())
        match index:
            case 1: timed_test()
            case 2: timed_test_debug()
            case _:
                print("  Unknown > ", end="")
                index = -1

def timed_test():
    print("Running... ", end="")
    
    start = time_ns()
    end = start + 1_000_000_000

    num = 0
    test_start()
    while time_ns() < end:
        calculate(num)
        num += 1
    print(f"Done.\nResult: {num - 1}")

def timed_test_debug():
    output = open("timings.csv", "w")
    output.write("Index,Time,Number\n")
    print("Running... ", end="")

    start = time_ns()
    end = start + 1_000_000_000

    num = 0
    test_start()
    prev, result = (0, 0)
    while time_ns() < end:
        prev = result
        result = calculate(num)
        num += 1

        time = time_ns() - start
        output.write(f"{num},{float(time) / 1e9},{result}\n")
    output.close()
    print(f"Done.\nResult: {num - 1} (Final Value {prev}).")

if __name__ == "__main__": main()
