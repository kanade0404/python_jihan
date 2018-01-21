# 入力値：硬貨 + 価格（ex:1 5 10 50 100 500 777 120）
# 硬貨 + 価格
coin_list = list(map(int, input().split()))
coin_num = len(coin_list)
# 合計
coin_sum = 0
# 価格
price = 0
# お釣り
change = 0

for i in range(coin_num):
    coin_chk = coin_list[i]
    if i == coin_num - 1:
        price = coin_chk
    elif coin_chk == 10 or coin_chk == 50 or coin_chk == 100 or coin_chk == 500:
        coin_sum = coin_sum + coin_chk
    elif coin_chk == 1 or coin_chk == 5:
        print("警告：" + str(coin_chk) + "は使えません")
    else:
        print("警告：" + str(coin_chk) + "は硬貨として適切な値ではありません")
change = coin_sum - price
print(str(change) + "円のお釣りです。ありがとうございました。")