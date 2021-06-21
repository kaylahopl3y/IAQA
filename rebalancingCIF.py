import pandas as pd

# Input assets into the CIF 
inp = {'Ticker': ['BTC', 'ETH', 'LTC'], 'MCAP': [20000, 10000, 5000], 'Price': [50, 25, 10]}

# Sort by highest MCAP
df = pd.DataFrame(inp)
df = df.sort_values(by=["MCAP"], ascending=False)
print(df)


# Find the total market cap by summing all the marketcaps
# Find the ratios by dividing each market cap by the sum
total_MCAP = df['MCAP'].sum()
df['MCAP_ratio'] = df['MCAP'].div(total_MCAP)
print(df)


# Ask for the user to input their desired asset cap and total capital
total_capital = input("Please enter your total capital:\n")
asset_cap = input("Please enter the asset cap:\n")

total_capital = float(total_capital)
asset_cap = float(asset_cap)

#  Max amount you can invest into any asset is asset cap * total capital 
max_invest= total_capital * asset_cap

# ticker = currency symbol, amount = the number of said asset that you own,
# usd = the value of usd that you have in each asset and pct = percent
ticker = []
amount = []
usd = []
pct = []

# len(df) is the number of assets / entries
# If asset cap < (1 / number of assets) then the amount invested = total_capital / len(df)
# pct will also be equal with 100 / len(df)
allocation_left = 1
if asset_cap < (1/len(df)):
    for index,rows in df.iterrows():
        amount_invested = total_capital/len(df)
        ticker.append(rows['Ticker'])
        amount.append(amount_invested/rows['Price'])
        usd.append(amount_invested)
        pct.append(100/len(df))
        
else: # If this is not the case we have our total_capital remaining
    rem_amount = total_capital

    # Going through every row to compare the MCAP_ratio with the asset_cap
    for index1,rows in df.iterrows():

        # If MCAP_ratio <= asset_cap 
        if rows['MCAP_ratio'] <= asset_cap:
            allocation = rows['MCAP_ratio']

            # Max you can put in is MCAP_ratio / 1 * rem_amount 
            max_amount_spend = (allocation/ allocation_left) * rem_amount
            ticker.append(rows['Ticker'])
            amount.append(max_amount_spend/rows['Price'])
            usd.append(max_amount_spend)
            pct.append(max_amount_spend * 100/total_capital)
            
        else: # Otherwise if the MCAP_ration > 1
            allocation_left -= rows['MCAP_ratio']

            # Your allocation into that asset = asset_cap and the max_amount_spend = max_invest seen before
            allocation = asset_cap
            max_amount_spend = max_invest
            if max_amount_spend <= rem_amount:
                rem_amount = rem_amount - max_amount_spend

                # Amount of the top asset
                amount.append(max_amount_spend/rows['Price'])
                ticker.append(rows['Ticker'])
                usd.append(max_amount_spend)
                pct.append(max_amount_spend * 100/total_capital)
            else: # The remaing assets are then added
                amount.append(rem_amount)
                usd.append(rem_amount)
                ticker.append(rows['Ticker'])
                amount.append(rem_amount/rows['Price'])

                # Remaining amount should be zero after balancing
                pct.append(rem_amount * 100/total_capital)
                rem_amount = 0


# New table with all the information
new_df = pd.DataFrame()
new_df["Ticker"] = ticker
new_df["Amount"] = amount
new_df["USD Value"] = usd
new_df["%"] = pct

# Printing 
print(new_df)

