item1=float(input("Enter price of item 1:"))
item2=float(input("Enter price of item 2:"))
item3=float(input("Enter price of item 3:"))
total=item1+item2+item3
discount=total*0.10
final_price=total-discount
print("Total price before discount:",total)
print("Discount amount:",discount)
print("Final price after discount:",final_price)
