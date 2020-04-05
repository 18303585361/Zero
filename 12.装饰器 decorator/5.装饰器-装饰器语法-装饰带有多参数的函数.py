# 装饰带有多参数的函数

def outer(func):
    def inner(who,name,*args,**kwargs):
        print("约妹子，拿到微信")
        func(who,name,*args,**kwargs)
        print("约妹子看电影")
    return inner
@outer
def love(who,name,*args,**kwargs):
    print(f'{who}跟{name}畅谈人生')
    print('完事吃了好多美食',args)
    print(f'看了一场{kwargs}电影')

love('小明','思思','火锅','辣条','7块钱的麻辣烫',mov='唐山大地震')

'''
love() ==> inner()
    love(...) ==> inner(...)
        inner(...) ==> love(...)
'''



















































