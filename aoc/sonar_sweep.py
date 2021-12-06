import logging

logging.basicConfig(filename="sonar_sweep.log", level=logging.DEBUG)


def sonar_sweep(data, deeper=True):
    increased = 0
    decreased = 0

    previous = -1

    for d in data:
        logging.debug(f"C: {d}\tP: {previous}")
        d_int = int(d)
        if previous == -1:
            logging.debug("FST")
        elif d_int > previous:
            logging.debug("INC")
            increased += 1
        elif d_int < previous:
            logging.debug("DEC")
            decreased += 1
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
        if previous == -1:
            logging.debug("FST")
        elif depth_total > previous:
            logging.debug("INC")
            increased += 1
        elif depth_total < previous:
            logging.debug("DEC")
            decreased += 1
        previous = depth_total

    return increased if deeper else decreased
