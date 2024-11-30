# IntraDay Trading Application
**Development Reference** : [How to Select Best IntraDay Trading Stocks](https://www.youtube.com/watch?v=c9Qb5QIltlg&t=95s)

**Dependencies** :
```
pip install pandastable.
sudo apt-get install python3-tk.
```
**Run Commands** :
`$ python3 trade.py`

**Limitations/Future Enhancements** :
* Need to Download the csv files manually each time.
* Webpage address hardcoded. #API's not available
* Processing depends on NSE maintaining the column/header structure. will need code updates if any of these change.

**Capabilities** :
* Load volatility csv/NSE 100 csv
* Perform Yearly and Daily Volatility calculations for the NSE100 Stocks.
* Pass the Modified data to a sheet application with sort, save and other sheets capability.
