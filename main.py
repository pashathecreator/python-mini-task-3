def parse_matrix(raw_input: str) -> list[list[float]]:
    formatted_input = list(raw_input.split(" | "))
    matrix = []
    for line in formatted_input:
        matrix.append(list(map(float, line.split())))
    return matrix

def main():
    raw_input = input()
    formatted_input = list(raw_input.split(" | "))
    matrix = []
    for line in formatted_input:
        matrix.append(list(map(float, line.split())))
    

if __name__ == "__main__":
    main()