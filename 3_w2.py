bookcost=24.95
numBooks = 60.0
def cost(numBooks):
  bulkBookCost = ((bookCost * 0.60) * numBooks)
  shippingCost = (3.0 + (0.75 * (numBooks - 1)))
  totalCost = bulkBookCost + shippingCost
  print(&quot;The total cost is:&quot;, totalCost)
cost(numBooks)
