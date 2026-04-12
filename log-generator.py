from datetime import datetime, timedelta
import random

LEVELS = ["INFO", "WARNING", "ERROR", "CRITICAL"]
WEIGHTS = [70, 20, 8, 2]  # percentages, roughly

start_time = datetime(2026,4,12,8,0,0)
time = start_time
messages = {
    "INFO": ['User login Successful', "Today's andy's birthday","Login failed","can you try harder?"],
    "WARNING": ['DB sync out of value',"Memory usage at 78%", "Retry attempt 2", "Unhandled exception in module X"],
    "ERROR": ['Panel temperature out of tolerance',"error error runnn!!","fatal error: system will crash in 10 minutes"],
    "CRITICAL": ['System Shutdown 101',"critical :its all over we're all gonna die"],
}
with open("sample_logs.txt","w") as f:
    for i in range(200):
        
        time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")

        level = random.choices(LEVELS,weights=WEIGHTS, k=1)[0]
        message = random.choice(messages[level])
        
        line = f"{time_stamp} {level} {message}"
        
        f.write(line + "\n")
        time = time + timedelta(seconds =random.randint(10,60))



    

