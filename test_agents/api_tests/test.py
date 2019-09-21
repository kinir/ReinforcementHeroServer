import requests
import threading
import time

def thread_function(i):
    start_time = time.time()
    url = "http://127.0.0.1:5000/api/test"

    response = requests.request("GET", url)

    print(f"Finished {i}, {response.text.strip()}, {time.time() - start_time}")


def main():
    start_time = time.time()
    threads = list()
    
    for i in range(8):
        x = threading.Thread(target=thread_function, args=(i,))
        threads.append(x)
        x.start()
        print(f"Started {i}")

    for x in threads:
        x.join()

    print(f"All {time.time() - start_time}")

if "__main__" == __name__:
    main()