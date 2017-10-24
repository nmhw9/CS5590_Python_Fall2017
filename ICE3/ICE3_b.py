iphonePrices = [{'Wallmart ': "iphone", 'ActualPrice' : 900, 'DiscountRate': 10},
                { 'BestBuy': "iphone",  'ActualPrice' : 900, 'DiscountRate': 20},
                { 'Target': "iphone",  'ActualPrice' : 900,'DiscountRate': 5}]
print("Intial Dictionary:")
print(iphonePrices)
print()

print("new dictionary with Discountprices:")
for each in iphonePrices:
    p = each.pop('ActualPrice')
    d = each.pop("DiscountRate")
    dp = p - (p * (d/100))
    each["DiscountPrice"]= dp

print(iphonePrices)


# i = {"h": 2, "g":3}
# print(i)
# k = i.pop("h")
# print(i)
# print(k)