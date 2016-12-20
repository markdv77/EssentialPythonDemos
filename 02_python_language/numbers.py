import weatherapp

nums = [1, 2, 3, 5, 6, 13, 21]
for idx, num in enumerate(nums):
    print('The {0}th number is {1}'.format(idx, num))

for day in weatherapp.get_days_of_week():
    print(day)
