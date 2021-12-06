import logging

logging.basicConfig(filename="sonar_sweep.log", level=logging.DEBUG)


def sonar_sweep(data, deeper=True):
    increased = 0
    decreased = 0

    previous = -1

    for d in data:
        logging.debug(f"C: {d}\tP: {previous}")
        d_int = int(d)
        res = compare(previous, d_int)
        increased += res[0]
        decreased += res[1]
        previous = d_int

    return increased if deeper else decreased


def sonar_sweep_window(data, window, deeper=True):
    increased = 0
    decreased = 0

    previous = -1

    for count, d in enumerate(data):
        depth_total = 0
        for tick in range(window):
            try:
                depth_total += int(data[count + tick])
            except IndexError:
                logging.info("We're done")
                break

        logging.debug(f"C: {depth_total}\tP: {previous}")
        res = compare(previous, depth_total)
        if res is None:
            continue
        increased += res[0]
        decreased += res[1]
        previous = depth_total

    return increased if deeper else decreased


def compare(previous, current):
    if previous == -1:
        return 0, 0
    elif current > previous:
        logging.debug("INC")
        return 1, 0
    elif current < previous:
        logging.debug("DEC")
        return 0, 1
