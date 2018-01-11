import sys

def exit_error(message, error_vars=""):
    print(message, error_vars)
    sys.exit(1)

def read_file(path: str) -> str:
    try:
        with open(path) as f:
            return f.read()
    except:
        exit_error("Can't read this file", path)

def parsing_map(buffer: str) -> list:
    map = []
    for line in buffer.strip().split("\n"):
       if not "#" in line:
         map.append(line.split(" "))
    return map

def print_map(map_size: int, map: list):
    padding = map_size * map_size
    for line in map:
        for elem in line:
            print("%s" % elem.rjust(padding), end='')
        print()

if __name__ == "__main__":
    if len(sys.argv) < 2 :
        exit_error("Usage pyhon3 main.py my_map.txt")
    buffer = read_file(sys.argv[1])
    SIZE_MAP, *MAP = parsing_map(buffer)
    print("MAP SIZE = ", int(SIZE_MAP[0]))
    print("MAP = ", MAP)
    print_map(int(SIZE_MAP[0]), MAP)
