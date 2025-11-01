# utils/scheduler.py
import schedule
import time
import threading
from datetime import datetime, timedelta

_jobs = []

def _reminder_job(text):
    # Simple reminder: prints to console. You can extend to system notifications.
    print("\n[REMINDER]", datetime.utcnow().isoformat(), " — Time to post:\n", text, "\n")

def schedule_post_reminder(text, minutes_from_now=60):
    run_at = datetime.utcnow() + timedelta(minutes=minutes_from_now)
    def job():
        _reminder_job(text)
    # schedule at specific time
    schedule_time = run_at.strftime("%H:%M")
    schedule.every().day.at(schedule_time).do(job)
    _jobs.append((schedule_time, job))
    print(f"Scheduled reminder at {schedule_time} UTC for post preview.")
    return True

def _run_scheduler_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

_scheduler_thread = None

def start_scheduler():
    global _scheduler_thread
    if _scheduler_thread and _scheduler_thread.is_alive():
        print("Scheduler already running.")
        return
    _scheduler_thread = threading.Thread(target=_run_scheduler_loop, daemon=True)
    _scheduler_thread.start()
    print("Scheduler started in background thread.")

if __name__ == "__main__":
    start_scheduler()
    schedule_post_reminder("Test post for scheduler", minutes_from_now=1)
    while True:
        time.sleep(1)
