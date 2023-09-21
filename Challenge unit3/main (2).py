def linearSearchProduct(productList,targetProduct):
  indices=[]
  for index, product in enumerate(productList):
    if product ==targetProduct:
      indices.append(index)
  return indices

#Example usage:

products=["Shoes","Boot","Loafer","Shoes","Sandal","Shoes"]
target="Shoes"
target2='Apple'
result=linearSearchProduct(products,target)
print (result)
    