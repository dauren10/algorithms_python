# fuzzysearch('car', 'cartwheel'); // true
# fuzzysearch('cwhl', 'cartwheel'); // true
# fuzzysearch('cwheel', 'cartwheel'); // true
# fuzzysearch('cartwheel', 'cartwheel'); // true
# fuzzysearch('cwheeel', 'cartwheel'); // false
# fuzzysearch('lw', 'cartwheel'); // false
# найти из первого аргумента что есть во втором включая порядок
 
# Yandex task
 
# Answer must be as write
 
# //true
# //false

# def test(str1,str2):
# for el in str1:
# if el in str2:
# return True
# else:
# return False
# print(test('car', 'cartwheel'))