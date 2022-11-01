# Electricity Prices
PRICE_ELECT_LOW_KWH = 5
PRICE_ELECT_MED_KWH = 10
PRICE_ELECT_HIGH_KWH = 15

LIMIT_KWH_LOW = 100
LIMIT_KWH_MED = 1000

# Water Prices
PRICE_WATER_LOW_LITERS = 50
PRICE_WATER_MED_LITERS = 60
PRICE_WATER_HIGH_LITERS = 70

LIMIT_METER_LOW = 250
LIMIT_METER_MED = 1500

# Implementation
bill_type = input(
    "Enter the type of bill you want to calculate: \n 1) Electricity\n 2) Water\n Your Choice: ")

if not (bill_type.isnumeric() and (int(bill_type) == 1 or int(bill_type) == 2)):
    print(f"Error: enter a number to choose a bill type from the list")
    exit()

# we are sure from previous steps that bill_type is a number
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

    if 0 < meter_reading <= LIMIT_KWH_LOW:
        bill_amount = meter_reading * PRICE_ELECT_LOW_KWH
    elif meter_reading > LIMIT_KWH_LOW and meter_reading <= LIMIT_KWH_MED:
        bill_amount = meter_reading * PRICE_ELECT_MED_KWH
    else:
        bill_amount = meter_reading * PRICE_ELECT_HIGH_KWH

    print(f"Your total Electricity bill is ${bill_amount}")

elif bill_type == 2:
    print(f"Calculating Water bill...")

    if 0 < meter_reading <= LIMIT_METER_LOW:
        bill_amount = meter_reading * PRICE_WATER_LOW_LITERS
    elif meter_reading > LIMIT_METER_LOW and meter_reading <= LIMIT_METER_MED:
        bill_amount = meter_reading * PRICE_WATER_MED_LITERS
    else:
        bill_amount = meter_reading * PRICE_WATER_HIGH_LITERS

    print(f"Your total Water bill is ${bill_amount}")

