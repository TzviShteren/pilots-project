from datetime import datetime, timedelta


def show_upcoming_date() -> str:
    the_date = datetime.now() + timedelta(days=1)
    return the_date.strftime("%Y-%m-%d 00:00:00")
