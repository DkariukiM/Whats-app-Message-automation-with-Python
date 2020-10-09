from apscheduler.schedulers.background import BlockingScheduler
from main import send_message


sched = BlockingScheduler()

#Schedule job_function to be called every two hours
sched.add_job(send_message, 'interval', seconds =2)#interval can be hours or seconds 

sched.start()