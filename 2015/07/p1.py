# 2021/xx/p1.py

import time


class op_node_t():
    def __init__(self, children, op, op_name):
        self._children = children
        self._op = op
        self._op_name = op_name
        self._cached = False

    def __str__(self):
        return f'op_node: {self._op_name} {self._children}'

    def get_value(self, node_map):
        if not self._cached:
            self._cached_value = self._op(self._children, node_map)
            self._cached = True

        return self._cached_value

    def reset(self):
        self._cached = False


def parse_node(line, ops):
    op_source, name = line.strip().split(' -> ')

    op_source = op_source.split(' ')

    if len(op_source) == 1:
        return name, op_node_t([op_source[0]], ops['MONAD'], 'MONAD')
    elif len(op_source) == 2:
        return name, op_node_t([op_source[1]], ops[op_source[0]], op_source[0])

    return name, op_node_t([op_source[0], op_source[2]], ops[op_source[1]], op_source[1])


def lookup_or_parse(target, nodes):
    return nodes[target].get_value(nodes) if target in nodes.keys() else int(target)


def get_ops():
    return {
        'AND': lambda children, nodes:
            lookup_or_parse(children[0], nodes) & lookup_or_parse(children[1], nodes),
        'OR': lambda children, nodes:
            lookup_or_parse(children[0], nodes) | lookup_or_parse(children[1], nodes),
        'LSHIFT': lambda children, nodes:
            lookup_or_parse(children[0], nodes) << lookup_or_parse(children[1], nodes),
        'RSHIFT': lambda children, nodes:
            lookup_or_parse(children[0], nodes) >> lookup_or_parse(children[1], nodes),
        'NOT': lambda children, nodes:
            ~lookup_or_parse(children[0], nodes),
        'MONAD': lambda children, nodes:
            lookup_or_parse(children[0], nodes),
    }


def parse_input(infn):
    ops = get_ops()

    with open(infn, 'r') as f:
        node_data = [parse_node(line, ops) for line in f.readlines()]

    node_map = dict(node_data)

    return node_map


def execute(infn, target):
    node_map = parse_input(infn)

    return node_map[target].get_value(node_map)


def main(infn, target):
    pre = time.perf_counter()

    result = execute(infn, target)

    post = time.perf_counter()

    print(result, 'in', (post - pre) * 1000, 'ms')


if __name__ == '__main__':
    main('test1.txt', 'd')
    main('input.txt', 'a')

