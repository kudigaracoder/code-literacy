icecreamDict = {
"flavor" : "rocky road",
"color" : "brown",
"calories" : 500,
"scoops" : [3,1]
}

print (icecreamDict)

customers = []

FirstCustomer = {
	"iceCreamOrdered" : True,
	"success" : 0.5
}

SecondCustomer = {
	"iceCreamOrdered" : False,
	"success" : 1.0
}

customers.append (FirstCustomer)
customers.append (SecondCustomer)

print (customers[0])

avgSuccessRate = (customers[0]["success"] + customers[1]["success"])/2

print (avgSuccessRate)