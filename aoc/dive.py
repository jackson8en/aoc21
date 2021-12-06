import logging
from operator import add

logging.basicConfig(filename="dive.log", level=logging.DEBUG)


def dive(data, start=[0, 0]):
    pos = start
    for d in data:
        inst, value = d.split()
        value = int(value)
        logging.debug(f"INST: {inst} \tVAL: {value}")
        if inst == "forward":
            pos = forward(pos, value)
        elif inst == "down":
            pos = down(pos, value)
        elif inst == "up":
            pos = up(pos, value)
    logging.debug(pos)
    return pos


def forward(pos, value):
    forward_mat = [value, 0]
    return list(map(add, pos, forward_mat))


def down(pos, value):
    down_mat = [0, value]
    return list(map(add, pos, down_mat))


def up(pos, value):
    up_mat = [0, -value]
    return list(map(add, pos, up_mat))
