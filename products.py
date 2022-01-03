import os # operating system # 檢查檔案是否存在


# function 越簡潔越好(只做單一事件)

# 讀取資料
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'item,price' in line:
                continue
            item, price = line.strip().split(',')
            products.append([item, price])
        print(products)
    return products

# 輸入新資料
def user_input(products):
    while True:
        item = input('請輸入商品名稱: ')
        if item == 'q' or item == '':
            print('')
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([item, price])
    return products

# 印出所有資料
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filname, products):
    with open(filname, 'w', encoding = 'utf-8') as f:
        f.write('item,price\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案是否存在
        products = read_file(filename)
    else:
        print('找不到檔案...')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)



main()