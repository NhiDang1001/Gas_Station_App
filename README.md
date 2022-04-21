# Gas_Station_App

- Link to code: [here](https://github.com/NhiDang1001/Gas_Station_App/blob/main/GasStationApp.py)

Gas station app. The app menu allows a customer to fill gas, and a manager to get sales information, reset totals, and change gas prices. 

### Functions used by customer
`fill():` Prompts the CUSTOMER to select the grade of fuel: Regular, Extra, or Premium.  (Prices 3.70$, 3.90$, 4.10$ per gallon: these prices are displayed before asking the customer to choose the grade of fuel.)

When the customer makes the selection, the selected grade and its price are displayed to the customer.

Next, the customer enters the number of gallons to be filled. .Price of the gas order is computed using a function.

Afterwards, `fill()` displays the price. (If the user enters 0 for gallons, the app displays ‘Operation Cancelled’)

### Functions used by manager
`sales():`  displays the total number of gallons sold of each grade of fuel, and total sales (in dollars), a single number across all orders.

`prices():` shows the per gallon prices for each grade of fuel. Then prompts the manager to enter the new price for each grade of fuel, one by one. If the price is not to be changed, the manager will hit Return without entering anything.

**Note:**
(Manager is not required to change all three prices at once. The manager may enter a new price for the regular grade, and respond to the next two prompts by just hitting Return, for example.  Handling this is the only difficult part of this problem. If you are unable to implement the feature as specified - manager hitting return without typing anything as a way of signaling no change in price).

If the manager hits Return without typing anything, the input is an empty string. 

**Update:**
After prompting the manager for the three new prices, the manager is prompted again for yes or no to updating prices, and the update proceeds only if confirmed.

Subsequent to any price change, any customer trying to fill gas will see the new prices.

`end_of_day():` shows the same information as the Sales option in the menu. Afterwards, prompts the manager,  whether to reset or not. If the manager says yes, the totals clear, and the app gets ready for a new day. (prices will not go back to original levels at the end of a day)
