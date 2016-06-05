import time
import webbrowser

total_breaks = 3
break_count = 0
break_time_seconds = 2 * 60 * 60

print("This program started on" + time.ctime()
while(break_count < total_breaks):
    time.sleep(break_time_seconds)
    webbrowser.open("https://www.youtube.com/watch?v=ru0K8uYEZWw")
    break_count = break_count + 1
