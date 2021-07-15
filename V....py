# i = 0
# print("H", end = "")
# while i < 1998:
#     print("m", end ="")
#     i += 1
# print(".")
import time

t0 = time.perf_counter()

print ("G", end = "")
for i in range (65517):
    print ("o", end = "")
print("d morning Vietnam!")

t1 = time.perf_counter()
print(t1-t0)