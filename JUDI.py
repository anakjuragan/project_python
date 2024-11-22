import random
import time
import sys

def clear():
    print("\n" * 100)

def typing_animation(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Untuk membuat baris baru setelah selesai

def main():
    saldo = 100
    typing_animation("Selamat datang di permainan Slot!", 0.1)

    while saldo >= 5:
        typing_animation(f"Saldo Anda: {saldo}", 0.1)
        typing_animation("Silakan pilih 5 angka dari 0 hingga 9 (pisahkan dengan spasi):", 0.1)

        # Input angka dari pengguna
        try:
            user_input = input("Masukkan 5 angka: ").split()
            user_numbers = [int(num) for num in user_input]
            if len(user_numbers) != 5 or any(num < 0 or num > 9 for num in user_numbers):
                typing_animation("Input tidak valid. Pastikan Anda memasukkan 5 angka antara 0 dan 9.", 0.1)
                continue
        except ValueError:
            typing_animation("Input tidak valid. Pastikan Anda memasukkan angka yang benar.", 0.1)
            continue
        
        saldo -= 5  # Mengurangi biaya spin
        typing_animation("Memutar slot...", 0.1)
        time.sleep(5)  # Jeda 5 detik sebelum menampilkan hasil

        # Generate 5 angka acak
        random_numbers = [random.randint(0, 9) for _ in range(5)]

        typing_animation("Angka acak: ", 0.1)
        for number in random_numbers:
            print(number)
            time.sleep(3)  # Jeda 3 detik sebelum menampilkan angka berikutnya

        # Cek kesamaan angka
        win_amount = 0
        for i in range(5):
            if user_numbers[i] == random_numbers[i]:
                win_amount += 10

        saldo += win_amount
        if win_amount > 0:
            typing_animation(f"Anda menang: {win_amount}!", 0.1)
        else:
            typing_animation("Tidak ada yang cocok. Coba lagi!", 0.1)

        if saldo < 5:
            typing_animation("Saldo Anda tidak cukup untuk bermain lagi. Terima kasih telah bermain!", 0.1)
            break
        
        choice = input("Apakah Anda ingin bermain lagi? (1.ya/2.tidak): ").strip().lower()
        if choice == '1':
            clear()  # Bersihkan layar sebelum memulai putaran baru
        else:
            break

if __name__ == "__main__":
    clear()
    main()
