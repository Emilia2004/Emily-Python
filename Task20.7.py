def log_messages(severity, *args, **kwargs):
    log_entry=f"[{severity}] "

    if "time" in kwargs:
        log_entry+=f"Time: {kwargs['time']}"
    else:
        log_entry+=f"Time: Current| "
    
    if "user" in kwargs:
        log_entry+=f"User: {kwargs['user']} |"

    for message in args:
        log_entry+=f"Message: {message} |"
    
    print(log_entry)

log_messages("info", "System started", "Initialization complete", time="2024-07-23 14:00:00", user="admin")
log_messages("error", "File not found", "Check file path", time="2024-07-23 14:05:00")
log_messages("warning", "Low disk space")
