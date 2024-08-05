def compound_interest(principal, rate, times_compounded, years):
    return principal * (1 + rate / times_compounded) ** (times_compounded * years)

def loan_payment(principal, rate, payments_per_year, years):
    monthly_rate = rate / payments_per_year
    number_of_payments = payments_per_year * years
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -number_of_payments)

def investment_return(initial_value, final_value):
    return ((final_value - initial_value) / initial_value) * 100

dict = {
    'compound_interest': compound_interest,
    'loan_payment': loan_payment,
    'investment_return': investment_return,
}

def financial_calculator(operation,**kwargs):
    op = dict[operation]
    return op(**kwargs)

operator = input("Enter operator (compound_interest,loan_payment,investment_return): ")
if operator == "compound_interest":
    princ = int(input("Enter principal: "))
    rat = int(input("Enter rate: "))
    time_comp = int(input("Enter compound times: "))
    year = int(input("Enter years: "))
    print("The compound interest is:",financial_calculator(operator,principal=princ,rate=rat,times_compounded=time_comp,years=year))
if operator == "loan_payment":
    princ  = int(input("Enter principal: "))
    rat = int(input("Enter rate: "))
    pay_year = int(input("Enter payments per year: "))
    year = int(input("Enter years: "))
    print("The loan payment is:",financial_calculator(operator,principal=princ,rate=rat,payments_per_year=pay_year,years=year))
if operator == "investment_return":
    init_value = int(input("Enter initial value: "))
    fin_value = int(input("Enter fianl value: "))
    print("Investment return is:",financial_calculator(operator,initial_value=init_value,final_value=fin_value))



