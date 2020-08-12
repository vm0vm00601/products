# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)   # p = [name, price] 等於789三行
	products.append(p)   # products.append([name, price])等於7~10四行
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])


# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:   # 'w' 寫入模式
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  # open只有打開檔案, 有write才會寫入
# \n 是換行	
# 離開with架構就會自動close 	