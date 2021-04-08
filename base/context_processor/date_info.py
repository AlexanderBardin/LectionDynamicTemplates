from datetime import date


def current_date(request):
    return {
        "my_date": date.today()
    }