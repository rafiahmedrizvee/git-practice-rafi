from datetime import datetime
from utils import add, subtract

print("Name: Rafi")
print("Today's Date:", datetime.today().date())

print("Add:", add(5, 3))
print("Subtract:", subtract(5, 3))

from utils import divide

print("Divide:", divide(10, 2))
print("Divide by zero:", divide(10, 0))