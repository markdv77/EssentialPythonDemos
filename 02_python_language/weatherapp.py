import random


def get_days_of_week():
    return ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']


def get_random_weather_report():
    """
    This function returns a totally fake weather report.
    :return: a fake report
    """
    reports = ['sunny', 'hot', 'dusty', 'windy', 'smoggy', 'rainy']
    index = random.randint(0, len(reports) - 1)
    return reports[index]


def main():
    days = get_days_of_week()

    # Let's get the report for each day
    for day in days:
        report = get_random_weather_report()
        text = None
        if day == 'sat' or day == 'sun':
            text = 'Lovely weekend day on {0}: {1}'.format(day, report)
        else:
            text = 'The weather on {0} will be {1}'.format(day, report)

        print(text)

if __name__ == '__main__':
    main()
