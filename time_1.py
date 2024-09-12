import math
total_seconds=int(input("Enter the total number of seconds:"))
hrs=total_seconds//3600
rem_sec=total_seconds%3600
mins=rem_sec//60
secs=rem_sec%60
print(f"{hrs}hour(s),{mins}minute(s),{secs}second(s)")
