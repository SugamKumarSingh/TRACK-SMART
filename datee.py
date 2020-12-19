from datetime import date
import pandas as pd

today = date.today()

d1 = today.strftime("%d/%m/%Y")

print("Today's date:", d1)


