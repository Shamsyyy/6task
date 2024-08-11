def reverse_array(n, numbers):
  """перевернуть массив чисел"""
  return numbers[::-1]

def rearrange_array(n, numbers):
  """изменить порядок элементов массива"""
  rearranged = []
  for i in range(n):
      if i % 2 == 0:
          rearranged.append(numbers[n - 1 - i // 2])
      else:
          rearranged.append(numbers[i // 2])
  return rearranged

if __name__ == "__main__":
  # Задание 1
  N1 = int(input("введите количество чисел для задания 1: "))
  numbers1 = [int(input()) for _ in range(N1)]
  print("перевернутый массив:", reverse_array(N1, numbers1))

  # Задание 2
  N2 = int(input("введите количество чисел для задания 2: "))
  numbers2 = list(map(int, input("введите числа через пробел: ").split()))
  print("измененный массив:", rearrange_array(N2, numbers2))