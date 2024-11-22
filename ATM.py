import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

saldo = 1000000

while True:
    print("=========================================================")
    print("|               Program ATM BANK CEMGURIA               |")
    print("=========================================================")

    print("Pilih bahasa")
    print("1. Bahasa Indonesia")
    print("2. English")
    print("3. 中文")
    bahasa = int(input("Pilih : "))
    clear()

    if bahasa == 1:  # Bahasa Indonesia
        print("1. Cek Saldo")
        print("2. Penarikan")
        print("3. Transfer")
        transaksi = int(input("Pilih : "))

        if transaksi == 1:
            print("Saldo anda tinggal : ", saldo)
            choice = int(input('Apakah Anda ingin memilih lagi? (1.yes/2.tidak): '))
            clear()
            if choice == 2:
                break

        elif transaksi == 2:
            print("Penarikan")
            print("1.  50.000")
            print("2.  100.000")
            print("3.  200.000")
            print("4.  300.000")
            print("5.  jumlah lainnya")
            penarikan = int(input("Pilih : "))

            if penarikan == 1:
                tp = 50000
            elif penarikan == 2:
                tp = 100000
            elif penarikan == 3:
                tp = 200000
            elif penarikan == 4:
                tp = 300000
            elif penarikan == 5:
                tp = int(input("Nominal : "))
            else:
                print("Transaksi Gagal")
                continue

            if tp > saldo:
                print("Saldo tidak mencukupi untuk penarikan.")
            else:
                saldo -= tp  # Update saldo setelah penarikan
                print("Penarikan sebanyak : ", tp)
                print("Sisa saldo anda : ", saldo)
                choice = int(input('Apakah Anda ingin memilih lagi? (1.yes/2.tidak): '))
                clear()
                if choice == 2:
                    break

        elif transaksi == 3:
            clear()
            print("Bank tujuan")
            print("1. BANK NAGARI")
            print("2. BANK BRI")
            print("3. BANK BNI")
            print("4. BANK BSI")
            bank = int(input("Masukkan tujuan BANK           : "))
            nama = ['Muhammad Raihan', 'Rafi Ahmad', 'Ahmad Bariq Maulana', 'Lionel Messi', 'Deni Satria']
            namarandom = random.choice(nama)
            clear()

            if bank == 1:
                admin = 10000
                nb = 'BANK NAGARI'
            elif bank == 2:
                admin = 5000
                nb = 'BANK BRI'
            elif bank == 3:
                admin = 2500
                nb = 'BANK BNI'
            elif bank == 4:
                admin = 3000
                nb = 'BANK BSI'
            else:
                print("Bank tidak valid.")
                continue

            nt = str(input("Masukkan Nomor Rekening tujuan  : "))
            np = int(input("Nominal Transfer                : "))

            if np + admin > saldo:
                print("Saldo tidak mencukupi untuk transfer.")
            else:
                saldo -= np + admin  # Update saldo setelah transfer
                clear()
                print("     Transaksi Berhasil    ")
                print("Nomor rekening tujuan          : ", nt)
                print("BANK                           : ", nb)
                print("Nama Pengguna tujuan           : ", namarandom)
                print("Nominal Transfer               : ", np)
                print("Biaya Admin                    : ", admin)
                print("Sisa Saldo anda                : ", saldo)
                choice = int(input('Apakah Anda ingin memilih lagi? (1.yes/2.tidak): '))
                clear()
                if choice == 2:
                    break

    elif bahasa == 2:  # English
        print("1. Check Balance")
        print("2. Withdrawal")
        print("3. Transfer")
        transaksi = int(input("Select : "))

        if transaksi == 1:
            print("Your remaining balance is: ", saldo)
            choice = int(input('Would you like to choose again? (1.yes/2.no): '))
            clear()
            if choice == 2:
                break

        elif transaksi == 2:
            print("Withdrawal")
            print("1.  50,000")
            print("2.  100,000")
            print("3.  200,000")
            print("4.  300,000")
            print("5.  Other amount")
            penarikan = int(input("Select : "))

            if penarikan == 1:
                tp = 50000
            elif penarikan == 2:
                tp = 100000
            elif penarikan == 3:
                tp = 200000
            elif penarikan == 4:
                tp = 300000
            elif penarikan == 5:
                tp = int(input("Amount : "))
            else:
                print("Transaction Failed")
                continue

            if tp > saldo:
                print("Insufficient balance for withdrawal.")
            else:
                saldo -= tp  # Update balance after withdrawal
                print("Withdrawal amount: ", tp)
                print("Your remaining balance: ", saldo)
                choice = int(input('Would you like to choose again? (1.yes/2.no): '))
                clear()
                if choice == 2:
                    break

        elif transaksi == 3:
            clear()
            print("Destination Bank")
            print("1. BANK NAGARI")
            print("2. BANK BRI")
            print("3. BANK BNI")
            print("4. BANK BSI")
            bank = int(input("Enter the destination BANK           : "))
            nama = ['Muhammad Raihan', 'Rafi Ahmad', 'Ahmad Bariq Maulana', 'Lionel Messi', 'Deni Satria']
            namarandom = random.choice(nama)
            clear()

            if bank == 1:
                admin = 10000
                nb = 'BANK NAGARI'
            elif bank == 2:
                admin = 5000
                nb = 'BANK BRI'
            elif bank == 3:
                admin = 2500
                nb = 'BANK BNI'
            elif bank == 4:
                admin = 3000
                nb = 'BANK BSI'
            else:
                print("Invalid bank.")
                continue

            nt = str(input("Enter destination Account Number  : "))
            np = int(input("Transfer Amount                  : "))

            if np + admin > saldo:
                print("Insufficient balance for transfer.")
            else:
                saldo -= np + admin  # Update balance after transfer
                clear()
                print("     Transaction Successful    ")
                print("Destination account number       : ", nt)
                print("BANK                             : ", nb)
                print("Recipient's Name                 : ", namarandom)
                print("Transfer Amount                  : ", np)
                print("Admin Fee                        : ", admin)
                print("Your remaining balance            : ", saldo)
                choice = int(input('Would you like to choose again? (1.yes/2.no): '))
                clear()
                if choice == 2:
                    break

    elif bahasa == 3:  # 中文
        print("1. 查询余额")
        print("2. 提款")
        print("3. 转账")
        transaksi = int(input("选择 : "))

        if transaksi == 1:
            print("您剩余的余额为: ", saldo)
            choice = int(input('您想重新选择吗? (1.是/2.否): '))
            clear()
            if choice == 2:
                break

        elif transaksi == 2:
            print("提款")
            print("1.  50,000")
            print("2.  100,000")
            print("3.  200,000")
            print("4.  300,000")
            print("5.  其他金额")
            penarikan = int(input("选择 : "))

            if penarikan == 1:
                tp = 50000
            elif penarikan == 2:
                tp = 100000
            elif penarikan == 3:
                tp = 200000
            elif penarikan == 4:
                tp = 300000
            elif penarikan == 5:
                tp = int(input("金额 : "))
            else:
                print("交易失败")
                continue

            if tp > saldo:
                print("余额不足，无法提款。")
            else:
                saldo -= tp  # 更新提款后的余额
                print("提款金额: ", tp)
                print("您剩余的余额: ", saldo)
                choice = int(input('您想重新选择吗? (1.是/2.否): '))
                clear()
                if choice == 2:
                    break

        elif transaksi == 3:
            clear()
            print("目的银行")
            print("1. BANK NAGARI")
            print("2. BANK BRI")
            print("3. BANK BNI")
            print("4. BANK BSI")
            bank = int(input("输入目的银行           : "))
            nama = ['Muhammad Raihan', 'Rafi Ahmad', 'Ahmad Bariq Maulana', 'Lionel Messi', 'Deni Satria']
            namarandom = random.choice(nama)
            clear()

            if bank == 1:
                admin = 10000
                nb = 'BANK NAGARI'
            elif bank == 2:
                admin = 5000
                nb = 'BANK BRI'
            elif bank == 3:
                admin = 2500
                nb = 'BANK BNI'
            elif bank == 4:
                admin = 3000
                nb = 'BANK BSI'
            else:
                print("无效的银行。")
                continue

            nt = str(input("输入目的账户号码  : "))
            np = int(input("转账金额                  : "))

            if np + admin > saldo:
                print("转账余额不足。")
            else:
                saldo -= np + admin  # 更新转账后的余额
                clear()
                print("     交易成功    ")
                print("目的账户号码       : ", nt)
                print("银行              : ", nb)
                print("收款人姓名        : ", namarandom)
                print("转账金额          : ", np)
                print("手续费            : ", admin)
                print("您剩余的余额      : ", saldo)
                choice = int(input('您想重新选择吗? (1.是/2.否): '))
                clear()
                if choice == 2:
                    break

    else:
        print("语言选项不可用。")
        choice = int(input('您想重新选择吗? (1.是/2.否): '))
        clear()
        if choice == 2:
            break
