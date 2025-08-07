bookCost=24.95
numBooks = 60.0
def cost(numBooks):
  bulkBookCost = ((bookCost * 0.60) * numBooks)
  shippingCost = (3.0 + (0.75 * (numBooks - 1)))
  totalCost = bulkBookCost + shippingCost
  print("The total cost is: ", totalCost)
cost(numBooks)
