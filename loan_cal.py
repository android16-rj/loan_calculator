import math
import argparse

parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", type=str, choices=["diff", "annuity"], help="enter the type whether diff or annuity")
parser.add_argument("--periods", type=int, help="Period Count")
parser.add_argument("--principal", type=float, help="Principal Amount")
parser.add_argument("--interest", type=float, help="Interest Rate")
parser.add_argument("--payment", type=float, help="Monthly Payments")
args = parser.parse_args()
if args.type is None:
    print("Incorrect parameters")
elif args.type not in ["diff", "annuity"]:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif args.type == "diff":
    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters")
    else:
        i = args.interest / (12 * 100)
        differentiated_payment = []
        for _i in range(1, args.periods + 1):
            d = math.ceil((args.principal/args.periods) + i * (args.principal - (args.principal * (_i-1)/args.periods)))
            differentiated_payment.append(d)
            print("Month {0}: payment is {1}".format(_i, d))
        over_payment = int(sum(differentiated_payment) - args.principal)
        print()
        print("Overpayment = {0}".format(over_payment))

elif args.type == "annuity":

    if args.principal is not None and args.periods is not None and args.interest is not None:
        i = args.interest / (12 * 100)
        annuity_payment = (math.ceil(args.principal * (i * (1 + i) ** args.periods) / (((1 + i) ** args.periods) - 1)))
        over_payment = int(annuity_payment * args.periods - args.principal)
        print(f"Your annuity payment = {annuity_payment}!")
        print(f"Overpayment = {over_payment}")
    elif args.payment is not None and args.principal is not None and args.interest is not None:
        i = args.interest / (12 * 100)
        z = (math.ceil(math.log(args.payment / (args.payment - (i * args.principal)), (1 + float(i)))))
        over_payment = int((z * args.payment) - args.principal)
        if z % 12 == 0:
            print("It will take " + str(z // 12) + " years to repay this loan!")
        elif z // 12 == 1:
            print("It will take " + str(z // 12) + " year and " + str(z % 12) + " months to repay this loan!")
        elif z // 12 == 1 and z % 12 == 0:  # improve in github
            print("It will take " + str(z // 12) + " year to repay this loan!")
        elif z < 12:
            print("It will take " + str(z) + " months to repay this loan!")
        elif z == 1:
            print("It will take " + str(z) + "month to repay this loan!")
        else:
            print("It will take " + str(z // 12) + " years and " + str(z % 12) + " months to repay this loan!")
        print("Overpayment = " + str(over_payment))
    elif args.payment is not None and args.periods is not None and args.interest is not None:
        i = args.interest / (12 * 100)
        z = (math.floor(args.payment / ((i * (1 + i) ** args.periods) / (((1 + i) ** args.periods) - 1))))
        over_payment = int(args.payment * args.periods - z)
        print(f'Your loan principal = {z}!')
        print(f'Overpayment = {over_payment}')
    else:
        print("Incorrect parameters")
