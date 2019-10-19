import requests
import threading
import time
import multiprocessing

def thread_function(i):
    start_time = time.time()
    url = f"http://127.0.0.1:5000/api/test/{i}"

    response = requests.request("GET", url)

    print(f"Finished {i}, {response.text.strip()}, {time.time() - start_time}")


def main():
    start_time = time.time()
    workers = list()
    
    for i in range(2):
        #x = threading.Thread(target=thread_function, args=(i,))
        x = multiprocessing.Process(target=thread_function, args=(i,))
        workers.append(x)
        x.start()
        print(f"Started {i}")
        time.sleep(5)

    for x in workers:
        x.join()

    print(f"All {time.time() - start_time}")

if "__main__" == __name__:
    main()