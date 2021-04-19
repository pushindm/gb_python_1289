# calculate simple fin. report
def fin_report(r, c):
    p = r - c
    if p < 0:
        print(f"Your firm has negative profit equals to {p:.2f} rubles")
    else:
        print(f"Your firm has positive profit equals to {p:.2f} rubles")
        p_proceeds = p / r
        print(f"Your profitability index is {p_proceeds:.2f}")
    return p


def ppe_calculation(p, n):
    print(f"Your profitability per employee is equal to {p / n:.02f}")


user_revenue, user_costs = input("Enter value of revenue and total costs: ").split(" ")
profit = fin_report(float(user_revenue), float(user_costs))
n_employers = float(input("Enter number of employers: "))
ppe_calculation(profit, n_employers)
