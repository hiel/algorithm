import queue

q = queue.Queue(maxsize=1)

try:
    print(q.get_nowait())
except queue.Empty:
    print('EMPTY!')

try:
    q.put_nowait(1)
    q.put_nowait(2)
except queue.Full:
    print('FULL!')
