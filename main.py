import matplotlib.pyplot as plt
from twelve_data import TwelveData
import numpy as np


currency_pair = "USD/PLN"
ticker = ["GOLD"]
prices_PLN = []

twelve_data = TwelveData()
print(twelve_data.get_all_data(ticker))

security_dataset = twelve_data.get_specific_data(ticker, "close")
fx_dataset = twelve_data.get_specific_data(currency_pair, "close")

time = [i for i in range(0, len(security_dataset))][::-1]
security_in_pln = [a * b for a, b in zip(security_dataset, fx_dataset)]

all_quantiles = [
    np.quantile(security_in_pln, .25),
    np.quantile(security_in_pln, .50),
    np.quantile(security_in_pln, .75),
]

plt.plot(
    time,
    security_in_pln,
    linewidth=0.75,
)
plt.plot(
    time,
    [all_quantiles for i in range(0, len(security_in_pln))],
    linestyle='dashed',
    color='black',
    linewidth=0.75,

)
plt.show()
