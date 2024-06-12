import time

current_timestamp = time.time()
print(time.time())
print(f"Current timestamp: {current_timestamp}")

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_timestamp))
print(f"Formatted time: {formatted_time}")
