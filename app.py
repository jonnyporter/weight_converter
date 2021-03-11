while True:
    weight = input("Weight: ")
    try:
        float(weight)
    except ValueError:
        print("This is not a number")
        break
    unit = input("(L)bs or (K)gs: ").upper()
    def lbs_convert() -> str:
        num = round(0.45359237 * float(weight), 1)
        return str(num) + " kilos"
    def kgs_convert() -> str:
        num = round(2.2046226218 * float(weight), 1)
        return str(num) + " pounds"
    def final_statement(unit_converter):
        print(f"You are {unit_converter}")
    def result():
        if unit == "L":
            final_statement(lbs_convert())
        elif unit == "K":
            final_statement(kgs_convert())
        else:
            print("try again")
    result()
