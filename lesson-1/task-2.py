# convert time in necessary format
def convert_time(t):
    h = t // 3600
    m = (t - h*3600) // 60
    s = (t - h*3600) % 60
    return h, m, s


# main
user_value = float(input("Enter execution time in seconds: "))
time = convert_time(user_value)
print(f"Your time (hh:mm:ss): {int(time[0]):02d}:{int(time[1]):02d}:{int(time[2]):02d}")
