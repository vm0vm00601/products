products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = []
	p.append(name)
	p.append(price)   # p = [name, price] 等於789三行
	products.append(p)   # products.append([name, price])等於7~10四行
print(products)

for p in products:
	print(p[0], '的價格是', p[1])


# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding='utf-8') as f:   # 'w' 寫入模式
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  # open只有打開檔案, 有write才會寫入
# \n 是換行	
# 離開with架構就會自動close 	