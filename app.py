from flask import Flask, request, jsonify
import math, time
import matplotlib.pyplot as plt

app = Flask(__name__)

def interpolation_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high and key >= arr[low] and key <= arr[high]:
        if low == high:
            return low if arr[low] == key else -1
        pos = low + int(((high - low) / (arr[high] - arr[low])) * (key - arr[low]))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    return -1

@app.route("/search")
def search():
    # Parameters from query string
    n = int(request.args.get("n", 100))
    key = int(request.args.get("key", 50))

    arr = [i * 10 for i in range(1, n + 1)]
    start = time.perf_counter()
    result = interpolation_search(arr, key)
    end = time.perf_counter()

    return jsonify({
        "array_size": n,
        "key": key,
        "result_index": result,
        "execution_time_microseconds": (end - start) * 1e6,
        "complexity": {
            "best": "O(1)",
            "average": "O(log log n)",
            "worst": "O(n)",
            "space": "O(1)"
        }
    })

if __name__ == "__main__":
    app.run()
