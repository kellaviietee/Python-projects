"""Cha-ching."""

amount = int(input("Enter a sum: "))
coins = 0

mod_50 = amount % 50
coins += (amount - mod_50) / 50
mod_20 = mod_50 % 20
coins += (mod_50 - mod_20) / 20
mod_10 = mod_20 % 10
coins += (mod_20 - mod_10) / 10
mod_5 = mod_10 % 5
coins += (mod_10 - mod_5) / 5 + mod_5
print(f"Amount of coins needed: {coins}")
