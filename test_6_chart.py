import numpy as np
import time
import multiprocessing as mp

def composite_sine_generator(n_points=500, seed=0):
    x = np.linspace(0, 499, n_points)
    offsets = [50, 52, 48, 55, 47, 51]
    while True:
        i = time.time() * 9.0 + seed * 25
        y = offsets[seed] + \
            25 * np.sin((x + i) / 8.3) + \
            10 * np.sin((x + i) / 7.5) - \
            5 * np.sin((x + i) / 1.5)
        y += 1.0 * np.random.randn(n_points)
        yield x.tolist(), y.tolist()


def data_producer(queue, stop_event):
    """Process riêng - chỉ sinh dữ liệu sine"""
    generators = [composite_sine_generator(seed=i) for i in range(6)]
    while not stop_event.is_set():
        try:
            data = [next(gen) for gen in generators]
            if not queue.full():
                queue.put(data)
            time.sleep(0.006)
        except:
            break