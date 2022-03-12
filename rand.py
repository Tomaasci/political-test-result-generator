import random;
num = input("How many links do you want to get?     ");
for x in range(int(num)):
 print ("https://www.ideoshapes.com/results.html?scores=" + str(random.randint(-10, 10)) + "," +  str(random.randint(-10, 10)) + "," + str(random.randint(-10, 10)) + "," + str(random.randint(-10, 10)) + "," + str(random.randint(-10, 10)) + "," + str(random.randint(-10, 10)) + "," + str(random.randint(-10, 10)) + "," + str(random.randint(-10, 10)) + "+&max=10,10,10,10,10,10,10,10&v=1.1")
