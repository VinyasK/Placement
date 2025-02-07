sales_list=[2000,3000,5500,7000,6400,10000,9999]

highest_sale=max(sales_list) //gives highest value from list

index=sales_list.index(highest_sale) //gives the index value of highest_sale value

print("Day {} has highest sales of {}".format(index,highest_sale))
