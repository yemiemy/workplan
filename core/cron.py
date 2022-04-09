from django_cron import CronJobBase, Schedule

class WorkerUpdateCron(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'core.WorkerUpdateCron'    # a unique code

    def do(self):
        print("This should work")    # do your thing here
