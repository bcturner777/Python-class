def computepay(r, h):
	if h <= 40 :
		p = h * r
	else :
		p = r * 40 + (r * 1.5 * (h - 40))
	return p

input = raw_input("Enter Hours: ")
hours = float(input)
input2 = raw_input ("Enter Hourly Rate: ")
rate = float(input2)

pay = computepay(rate, hours)
pay = str(pay)
text = "Your total pay = $"
print text + pay
