
'''flight_price_short = float(input("Price of flights for short trip (incl. bags): £"))
flight_price_long = float(input("Price of flights for long trip (incl. bags): £"))
parking_short = float(input("Price of parking for short trip: £"))
parking_long = float(input("Price of parking for long trip: £"))
accom_price_short = float(input("Price of accommodation for short trip: £"))
accom_price_long = float(input("Price of accommodation for long trip: £"))
accom_rating_short = input("Is your accommodation budget/ nice/ luxury? ")
accom_rating_long = input("Is your accommodation budget/ nice/ luxury? ")
spending_short = float(input("What is your spending allowance for the short trip? £"))
spending_long = float(input("What is your spending allowance for the long trip? £"))
length_holiday_short = float(input("For how many days would you go away for the short trip? "))
length_holiday_long = float(input("For how many days would you go away for the long trip? "))
current_total_budget = float(input("How much money do you have for travel at the moment? "))
future_total_budget = float(input("How much do you save a month for travel? "))
additional_cost_short = float(input("What is the addition cost per day for the short trip e.g. car hire? £"))
additional_cost_long = float(input("What is the addition cost per day for the long trip e.g. car hire? £"))'''

flight_price_short = float(300)
flight_price_long = float(1500)

#the below amounts are totals
parking_short = float(50)
parking_long = float(200)
accom_price_short = float(400)
accom_price_long = float(400)
additional_cost_short = float(0)
additional_cost_long = float(450)

#the below rating is out 5
accom_rating_short = float(4.5)
accom_rating_long = float(4)

#the below is the spending allowance per day
spending_short = float(60)
spending_long = float(30)

length_holiday_short = float(6)
length_holiday_long = float(14)
#the below refers to Travel dedicated savings
current_total_budget = float(1000)
monthly_savings = float(300)

#TOTAL COST OF EACH HOLIDAY
short_total = flight_price_short + parking_short + accom_price_short + (spending_short * length_holiday_short) + additional_cost_short
print("Cost of the short holiday: " + str(round(short_total)))
long_total = flight_price_long + parking_long + accom_price_long + (spending_long * length_holiday_long) + additional_cost_long
print("Cost of the long holiday: " + str(round(long_total)))
#short_long_cost_ratio = long_total/ short_total
#print("Long-Short cost ratio is " + str(short_long_cost_ratio))
print("\n")

#VARIABLES
price_ratio = long_total/ short_total
days_of_short_holidays = price_ratio * length_holiday_short
response_difference_days = ""
def reduced_cost_short():
    reduced_amount_short = "£" + str(round(short_total - (((short_total/ length_holiday_short) - (long_total/ length_holiday_long)) * length_holiday_short), 2))
    return reduced_amount_short
def reduced_cost_long():
    reduced_amount_long = "£" + str(round(long_total - (((long_total/ length_holiday_long) - (short_total/ length_holiday_short)) * length_holiday_long), 2))
    return reduced_amount_long

#COST OF HOLIDAY IN TERMS OF DAYS LOST OR GAINED
if days_of_short_holidays < length_holiday_long:
    difference = length_holiday_long - days_of_short_holidays
    response_difference_days = "It will cost you " + str(round(difference, 1)) + " days for shorter, more frequent holidays.\nHowever, if you reduced the short trip cost to " \
                               + str(reduced_cost_short()) + " from " + "£" + str(round(short_total, 2)) + " you could mitigate this cost."
elif days_of_short_holidays > length_holiday_long:
    difference = days_of_short_holidays - length_holiday_long
    response_difference_days = "This means that for the same price as the long holiday, you get " + str(round(difference, 1)) + " days more of holiday.\nHowever, if you reduced the long trip cost to "\
                               + str(reduced_cost_long()) + " from " + "£" + str(round(long_total, 2)) + " you could mitigate this cost"
else:
    response_difference_days = "You get the same amount of holiday for your money with each holiday."

#SUMMARY OF THE DATA
print("You could do " + str(round(price_ratio, 1)) + " short trips for the price of the long one.\n\nBy doing shorter trips, you get " + str(round(days_of_short_holidays, 1)) \
      + " days of holiday spread out over " + str(round(price_ratio, 1)) + " trips VS " + str(round(length_holiday_long, 1)) \
      + " days of holiday all at once, in the same place.\n" \
      + response_difference_days + ".")


print("\n")

#print("Cost-Duration Ratio: the lower the number the better as you are getting more value for money")
cost_duration_short = short_total/ length_holiday_short
#print("Cost-Duration Ratio of the short: " + str(cost_duration_short))
cost_duration_long = long_total/ length_holiday_long
#print("Cost-Duration Ratio of the long holiday: " + str(cost_duration_long))
cost_duration_ratio = cost_duration_long/ cost_duration_short
'''if cost_duration_ratio > 1:
    print("The short trip is better value for money.\nThe cost-duration ratio is: " + str(cost_duration_ratio) \
          + "\nThe higher the number above 1, the better value the short trip is in comparison.\n The lower the number below 1, the better value the long trip is in comparison.")
else:
    print("The long trip is better value for money.\nThe cost-duration ratio is: " + str(cost_duration_ratio) \
          + "\nThe higher the number above 1, the better value the short trip is in comparison.\nThe lower the number below 1, the better value the long trip is in comparison.")
print("\n")'''
if 1< cost_duration_ratio <1.5:
    print("The short trip is better value for money than the long trip, but not by much.\nThe cost-duration ratio is: " + str(round(cost_duration_ratio, 2)))
elif 1.5<= cost_duration_ratio <2:
    print("The short trip is better value for money than the long trip.\nThe cost-duration ratio is: " + str(round(cost_duration_ratio, 2)))
elif cost_duration_ratio >=2:
    print("The short trip offers at least twice as much value for money.\nThe cost-duration ratio is: " + str(round(cost_duration_ratio, 2)))
elif 0.85< cost_duration_ratio <1:
    print("The long trip is better value for money than the short trip, but not by much.\nThe cost-duration ratio is: " + str(round(cost_duration_ratio, 2)))
elif 0.85<= cost_duration_ratio >0.5 :
    print("The long trip is better value for money than the short trip.\nThe cost-duration ratio is: " + str(round(cost_duration_ratio, 2)))
elif cost_duration_ratio <=0.5:
    print("The long trip is significantly better value for money than the short trip.\nThe cost-duration ratio is: " + str(round(cost_duration_ratio, 2)))
else:
    print("They are the same value for money")
print("\n")



#print("Quality Ratio: the higher the number the more luxury you are getting on your trip based on accommodation and daily spending")
quality_short = (accom_rating_short * 10) + spending_short
#print("Quality Ratio for the short holiday: " + str(quality_short))
quality_long = (accom_rating_long * 10) + spending_long
#print("Quality Ratio for the long holiday: " + str(quality_long))
quality_ratio = quality_long / quality_short
#print(quality_ratio)
if 1< quality_ratio <1.5:
    print("The long trip will offer more luxury than the short trip, but not by much.")
elif 1.5<= quality_ratio <2:
    print("The long trip will offer more luxury than the short trip.")
elif quality_ratio >=2:
    print("The long trip will offer at least twice as much more luxury than the short trip.")
elif 0.85< quality_ratio <1:
    print("The short trip will offer more luxury than the long trip, but not by much.")
elif 0.5< quality_ratio <=0.85:
    print("The short trip will offer more luxury than the long trip.")
elif quality_ratio <=0.5:
    print("The short trip will offer a significant amount more luxury than the long trip.")
else:
    print("The trips offer the same amount of luxury.")
print("\n")

def budget():
    if current_total_budget < long_total:
        save = round((long_total - current_total_budget) / monthly_savings, 1)
        print("You will need to save for " + str(save) + " months to afford the long holiday, based on your current savings\nand amount saved per month.")
    else:
        left_over = long_total - current_total_budget
        print("You will have " + str(left_over) + "left over after the long trip.")
    if current_total_budget < short_total:
        save1 = round((short_total - current_total_budget) / monthly_savings, 1)
        print("You will need to save for " + str(save1) + " months to afford the short holiday, based on your current savings\nand amount saved per month.")
    else:
        left_over1 = current_total_budget - short_total
        print("If you do the short holiday instead, you will have " + str(left_over1) + " left over for another holiday")

budget()


