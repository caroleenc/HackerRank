steps = 8
path = 'UDDDUDUU'
trajectory = 0
count = 0
status = 'neutral'

for step in path:
    temp_status = status
    if step.capitalize() == 'U':
        trajectory += 1 #'/'
        if trajectory > 0:
            status = 'mountain'
        elif trajectory == 0:
            status = 'neutral'
        print(trajectory, '/', status)
    elif step.capitalize() == 'D':
        trajectory -= 1 #'\\'
        if trajectory < 0:
            status = 'valley'
        elif trajectory == 0:
            status = 'neutral'
        if temp_status == 'neutral':
            count += 1
        print(trajectory, '\\', status)
# trajectory += '-'

print(count)