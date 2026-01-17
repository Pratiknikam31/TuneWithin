    scheduler_thread = threading.Thread(target=start_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()