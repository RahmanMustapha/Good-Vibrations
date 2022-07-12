import time, random, keyboard, numpy as np
from numpy import savetxt


latencies = np.zeros(30)
print("beginning visual latency test! Click q when you see it!")
 
for i, cur_latency in enumerate(latencies):
  time.sleep(random.randint(1,4))
  print("\nq")
  time_start = time.perf_counter()

  while True:
    if keyboard.is_pressed("q"):
      time_end = time.perf_counter() 
      print("You pressed q")
      break

  fractional_latency = time_end - time_start
  latency = np.round(fractional_latency, 2) * 100
  print("with latency: " + str(latency) + " ms\n")

  latencies[i] = latency

print(latencies.tolist())
print("\n")
print("average latency: " + str(np.mean(latencies)) + " ms")
savetxt('data.csv', latencies,fmt="%.2d", delimiter='.', newline = ", ")