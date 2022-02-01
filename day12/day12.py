from collections import defaultdict

def main(data):
    paths = defaultdict(set)
    for path in data:
        n1, n2 = path.split('-')
        paths[n1].add(n2)
        paths[n2].add(n1)

    def dfs(path=['start']):
        if path[-1] == 'end':
            return 1
        nodes_to_traverse = [node for node in paths[path[-1]] if ((node.isupper() or path.count(node) < 1))]
        return sum([dfs(path+[node]) for node in nodes_to_traverse])
    print(dfs())
    # Enter code here



if __name__ == "__main__":
    with open("day12_input_test.txt", 'r') as file:
        data = file.read().splitlines()
    main(data)
