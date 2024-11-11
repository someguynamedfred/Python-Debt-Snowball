def loan_sorter(loans):
    loans.sort(key=lambda x:x[0])

def loan_total(loans):
    total = 0
    for n in loans:
        total = total + n[0]
    return total

def payment(loans):
    for n in loans: 
        n[0] = n[0] + (n[0] * n[1])
        n[0] = n[0] - n[2]

def determine_total(loans, list_element):
    total = 0
    for n in loans:
        total = total + n[list_element]
    return total

def debt_snowball(loans, monthly_allocation):
    loan_sorter(loans)
    month = 1
    while loans != []:
        print("Month {}".format(month))
        minimum_payment_total = 0

        for n in loans:
            minimum_payment_total = minimum_payment_total + n[2]

        if n[0] > 0:

            extra_payment = monthly_allocation - minimum_payment_total

            loans[0][0] = loans[0][0] - extra_payment
            print("\tYou made an extra payment of ${:,.2f} to {}".format(extra_payment, loans[0][3]))

            payment(loans)

        if loans[0][0] < 0:
            loans.pop(0)

        if loans == []:
            print("\nYou will have paid off your loans in {} months!".format(month))
        else: 
            for n in loans:
                # do the formatting right here
                print("\t{} \t| payment = ${:,.2f} \t| remaining balance = ${:,.2f}".format(n[3],n[2],int(n[0])))
            print("\t" + "-"*72)
            print("\tTotals \t\t| payment = ${:,.2f} \t| remaining balance = ${:,.2f}\n".format((determine_total(loans,2) + extra_payment), determine_total(loans,0)))
            month += 1

# monthly payment
monthly_payment = int(input("what do you want to pay every month? "))

# months behind
# if you are behind on your mortgage, you can make it into its own line item by subtracting the current month from the initial month
months_behind = 11-5

# interest rates (this is calculated monthly so APR will need to be divided in 12) 
interest_credit_card = .20/12
interest_motorcycle = .12/12
interest_lge = .09/12

# actual debts
# loan_variable = [name, interest, min_payment]
# again, interest is calculated monthly so APR will need to be divided in 12
back_mortgage = [1127.87 * months_behind, 0, 200, "Back Mortgage"]
credit_card = [951.69, interest_credit_card, 60, "Credit Card"]
motorcycle_loan = [7540.08, interest_motorcycle, 202, "Motorcycle"]
lge_loan = [2627.46, interest_lge, 127, "LGE Loan"]

# student loans
# follows the same pattern as "actual debts"
# again, interest is calculated monthly so APR will need to be divided in 12
student_loan_1 = [3551, .02/12, (128/4), "Student Loan 1"]
student_loan_2 = [3551, .02/12, (128/4), "Student Loan 2"]
student_loan_3 = [2230, .02/12, (128/4), "Student Loan 3"]
student_loan_4 = [2216, .02/12, (128/4), "Student Loan 4"]

# total
# make sure that the "all_loans" list includes all relevant loan lists
all_loans = [back_mortgage,credit_card,motorcycle_loan,lge_loan,student_loan_1,student_loan_2,student_loan_3,student_loan_4]

# execute the script
debt_snowball(all_loans, monthly_payment)
