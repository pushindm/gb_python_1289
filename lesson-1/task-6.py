# calculate day X
def running_calculator(start_val, opt_val):
    i = 0
    inc = 0.1
    cur_val = start_val
    while cur_val < opt_val:
        i += 1
        cur_val = start_val*(1+inc)**(i-1)
        print(f"{i}-й день: {cur_val:.2f}")
    print(f"Ответ: на {i}-й день спортсмен достиг результата — не менее {cur_val:.0f} км.")


start_result, opt_result = input("Your data: ").split(' ')
running_calculator(float(start_result), float(opt_result))
