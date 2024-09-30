from utils.number_operation import kiem_tra_so_nt

inp = open("./src/2_sum_prime_number.inp", "r")

def kiem_tra_so_nt(so: int) -> bool:
  if so == 1:
    return False
  elif so == 2:
    return True
  else:
    for i in range(2, so):
        if so % i == 0:
            return False
  return True

def tinh_tong_so_nguyen_to(list_hang: list) -> int:
  tong = 0
  for number in list_hang:
    if kiem_tra_so_nt(number):
      tong += number
  return tong

list_hang_1 = [int(x) for x in inp.readline().split()]
list_hang_2 = [int(x) for x in inp.readline().split()]

with open("./build/2_sum_prime_number.out", "w") as out:
  out.writelines([
    f"Tong cac so nguyen to hang 1: {tinh_tong_so_nguyen_to(list_hang_1)}" + "\n",
    f"Tong cac so nguyen to hang 2: {tinh_tong_so_nguyen_to(list_hang_2)}"
  ])