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


def adv_dive(data, start=[0, 0], aim=0):
    pos = start
    aim = aim
    for d in data:
        inst, value = d.split()
        value = int(value)
        logging.debug(f"INST: {inst} \tVAL: {value}")
        if inst == "forward":
            pos = forward(pos, value, aim)
        elif inst == "down":
            aim = aim_down(aim, value)
        elif inst == "up":
            aim = aim_up(aim, value)
    logging.debug(pos)
    return pos


def forward(pos, value, aim=0):
    forward_mat = [value, value*aim]
    logging.debug(forward_mat)
    return [sum(x) for x in zip(pos, forward_mat)]


def down(pos, value):
    down_mat = [0, value]
    return [sum(x) for x in zip(pos, down_mat)]


def aim_down(aim, value):
    return aim + value


def up(pos, value):
    up_mat = [0, -value]
    return [sum(x) for x in zip(pos, up_mat)]


def aim_up(aim, value):
    return aim - value
