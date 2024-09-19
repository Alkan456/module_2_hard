import random
def get_code():
    number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3,21))
    code = random.choice(numbers)
    return code

def get_password(n):
    passdict = {}
    passdict.update({3:12, 4:13, 5:1423, 6:121524, 7:162534, 8:13172635, 9:1218273645})
    passdict.update({10:142319283746, 11:11029384756, 12:12131524111210394857})
    passdict.update({13:112211310495867, 14:1625341132123114105968})
    passdict.update({15:1214231142133124115106978, 16:1317263511521431341251161079})
    passdict.update({17:11621531441351261171089})
    passdict.update({18:12152418273645117216315414513612711810})
    passdict.update({19:118217316415514613712811910})
    passdict.update({20:13142319283746119218317416515614713812911})
    password =passdict.get(n)
    return password

n = get_code()
print('Шифр:', n)

paienumbers1 = list(range(1,n))
paienumbers2 = list(range(1,n))
pairs = []
result = ''

for a in paienumbers1:
    for b in paienumbers2:
        i = a
        j = b
        if i >= j:
            continue
        else:
            div = n % (i + j)
            if div == 0:
                pairs.append([i, j])
                result = result + str(i) + str(j)
print('Пары чисел:', pairs)
print('Введите пароль:', result)




