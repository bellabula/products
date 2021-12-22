# 檢查檔案是否存在
import os # operating system

products = []
if os.path.isfile('products.csv'):
    # 讀取檔案
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'item,price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('找不到檔案...')
    
# 輸入新資料
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    products.append([name, price])
print(products)        

# 印出所有資料
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('item,price\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')