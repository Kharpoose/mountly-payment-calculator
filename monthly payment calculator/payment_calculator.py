def main():
      print(" This is mountly payment loan calculator " + "\n")
      
      
      principal = float(input("Input the loan amount: "))
      apr = float(input("Input the annual interest rate: "))
      years = int(input("Input amount of year: "))
      
      
      mountly_interest_rate = apr / 1200
      amount_of_mounnth = years * 12
      mountly_payment = principal * mountly_interest_rate / (1 - (1 + mountly_interest_rate) ** (-amount_of_mounnth))
      
      
      print(f"The mountly pament for this loan is: {int(mountly_payment)}")
      
      
main()      