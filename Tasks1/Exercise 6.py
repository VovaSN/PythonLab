def evolutionOfCapital():
    startCapital = float(input("Enter started capital: "))
    interestRate = float(input("Enter interest rate in %: ")) / 100
    investmentPeriod = int(input("Enter investment period  in year: "))

    currentBalance = startCapital

    for year in range(1, investmentPeriod + 1):
        interestEarned = currentBalance * interestRate
        currentBalance += interestEarned

        print(f"{year} | {interestEarned:.2f} | {currentBalance:.1f}")
    
def yearsToDoubleCapital():
    interestRate = float(input("Enter interest rate in %: ")) / 100
    startCapital = float(input("Enter started capital in: "))

    targetCapital, years = startCapital * 2, 0

    print("\nYears\t Capital")
    while startCapital < targetCapital:
        interestEarned = startCapital * interestRate
        startCapital += interestEarned
        years += 1
        print(f"{years}\t {startCapital:.2f}")

    print(f"\nThe capital will double in {yearsToDoubleCapital()} years.")

evolutionOfCapital()
yearsToDoubleCapital()