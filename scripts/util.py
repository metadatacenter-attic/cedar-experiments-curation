import time
import sys


def log_progress(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    # slow down the rate at which the messages are printed
    if count % 1000 == 0 or percent == 100:
        sys.stdout.write("...%d%%, %d MB, %d KB/s, %d seconds passed\r" %
                         (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


def confirm(question):
    # raw_input returns the empty string for "enter"
    yes = {'yes', 'y'}
    no = {'no', 'n'}
    sys.stdout.write(question)
    choice = input().lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        sys.stdout.write("Please respond 'y' or 'n'")
