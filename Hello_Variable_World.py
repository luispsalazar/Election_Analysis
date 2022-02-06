from concurrent.futures.process import _threads_wakeups
from xmlrpc.client import boolean


name = "Luis"
country = "Ecuador"
age = 30
hourly_wage = 22
satisfied = True
daily_wage = 8 * hourly_wage
print(name,country,age,hourly_wage)
print(f"My daily wage is {daily_wage} and I am {satisfied}")