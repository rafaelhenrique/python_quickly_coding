from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    # import ipdb; ipdb.set_trace() # breakpoint
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Exemplo de uso
if __name__ == "__main__":
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            # import ipdb; ipdb.set_trace() # breakpoint
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
