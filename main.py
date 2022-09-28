# Electricity Prices
kwh_price_low = 5
kwh_price_med  = 10
kwh_price_high = 15

low_kwh_limit = 100
med_kwh_limit = 1000

# Water Prices
water_price_low = 50
water_price_med = 60
water_price_high = 70

low_water_limit = 250
med_water_limit = 1500

# Implementation
bill_type = input("Enter the type of bill you want to calculate: \n 1)Electricity \n 2)Water \n Your Choice: ")

if not (bill_type.isnumeric() and (int(bill_type) == 1 or int(bill_type) == 2)):
    print(f"Error: enter a number to choose a bill type from the list")
    exit()

bill_type = int(bill_type)
if bill_type == 1:
    meter_reading = input("Enter your electric meter reading in kwH: ")
elif bill_type == 2:
    meter_reading = input("Enter your water meter reading in m^3: ")

if not meter_reading.isnumeric():
    print("Error: Please enter a numerical meter reading")
    exit()

meter_reading = int(meter_reading)

if bill_type == 1:
    print(f"Calculating Electricity bill...")

    if meter_reading <= low_kwh_limit:
        bill_amount = meter_reading * kwh_price_low
    elif meter_reading > low_kwh_limit and meter_reading < med_kwh_limit:
        bill_amount = meter_reading * kwh_price_med
    else:
        bill_amount = meter_reading * kwh_price_high

    print(f"Your total Electricity bill is ${bill_amount}")

elif bill_type == 2:
    print(f"Calculating Water bill...")

    if meter_reading <= low_water_limit:
        bill_amount = meter_reading * water_price_low
    elif meter_reading > low_water_limit and meter_reading < med_water_limit:
        bill_amount = meter_reading * water_price_med
    else: 
        bill_amount = meter_reading * water_price_high

    print(f"Your total Water bill is ${bill_amount}")

