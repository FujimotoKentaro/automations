
from lib2to3.pgen2 import driver


def f(x):
    return x * 2
assert(f(1) == 2)
assert(f(3) == 6)


def g(x):
    return x.upper()
assert(g('hello') == 'HELLO')
assert(g('python') == 'PYTHON')


def pretty_print(name,cost_price,tax_rate):
    unit_cost_price = cost_price+cost_price*tax_rate/100
    return f'{cost_price}円の{name}を買ったら{unit_cost_price}円になりました'

assert(pretty_print('りんご', 100, 8) == '100円のりんごを買ったら108.0円になりました')
assert(pretty_print('みかん', 500, 8) == '500円のみかんを買ったら540.0円になりました')



def find_element(by,name):
    return driver.find_element(by,name)


assert(find_element(By.ID,'submit') == driver.find_element(By.ID,'submit'))
assert(find_element(By.XPATH,xpath) == driver.find_element(By.XPATH,xpath))

assert(f(2) == g(-2))


def h(x):
    return x**2 + x + 3


# 関数　ｆとｈを使いたい
a = f(2)
b = h(2 * 2)

def a():
    return 1

def b():
    return 2

def c():
    val_a = a()
    val_b = b()
    return val_a + val_b
