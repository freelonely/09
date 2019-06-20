from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time
import os

def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    print('Begin.....')
    scheduler = BlockingScheduler()

    #每个3秒执行一次
    # scheduler.add_job(tick,'cron', second='*/3', hour='*')

    #每天凌晨1点执行
    scheduler.add_job(tick, 'cron', hour='1', minute='0', second='0')
    scheduler.start()


    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
            scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()