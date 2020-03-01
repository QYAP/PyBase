# encoding: utf-8
# Author    : AP
# Datetime  : 2019/9/30 14:08
# Project   : BaseProject


from app.libs.build_in.reflect import reflect_func


# detail_exc_raised={11000:自定义Mongo报错类}


# detail_exc_raised={11000:自定义Mongo报错类}

def class_exc_raiser(default_exc_raised=None, detail_exc_raised: {str: object} = None):
    """
    类装饰器，为该类的每个自定义增加异常处理，并且可以被继承
    先判断错误类型是否符合unique_exc_raised，再判断是否符合detail_exc_raised，都不符合最后才抛出default_exc_raised
    detail_exc_raised:{error_int_code:exc_instance}
    """

    def inner(cls):
        funcs = reflect_func(cls)  # 获取类的所有方法
        for k_name, v_func in list(funcs.items()):
            if "self" in v_func.__code__.co_varnames:
                setattr(
                    cls,
                    k_name,
                    lambda self, *args, this_func=v_func, **kwargs:
                    instance_or_class_safe_run(self, this_func, *args, **kwargs)
                )
            elif "cls" in v_func.__code__.co_varnames:
                setattr(
                    cls,
                    k_name,
                    classmethod(
                        lambda cls, *args, this_func=v_func, **kwargs:
                        instance_or_class_safe_run(cls, this_func, *args, **kwargs)
                    )
                )
            else:
                setattr(
                    cls,
                    k_name,
                    staticmethod(
                        lambda *args, this_func=v_func, **kwargs: static_safe_run(this_func, *args, **kwargs)
                    )
                )

        @exc_process
        def instance_or_class_safe_run(self_or_cls, func, *args, **kwargs):
            return func(self_or_cls, *args, **kwargs)

        @exc_process
        def static_safe_run(func, *args, **kwargs):
            return func(*args, **kwargs)

        return cls

    def exc_process(fun):
        """
        异常处理
        """

        def inner(*args, **kwargs):
            try:
                return fun(*args, **kwargs)
            except Exception as e:

                if isinstance(detail_exc_raised, dict):
                    for err_code, exc in detail_exc_raised.items():
                        if getattr(e, "code", None) == err_code:
                            print("错误已经被处理！！！")
                    # raise exc

                if default_exc_raised is None:
                    print("错误已经被处理！！！")
                # raise e
                else:
                    print("错误已经被处理！！！")
            # raise detail_exc_raised

        return inner

    return inner


def classmethod_exc_wrapper(func):
    """
    装饰器类，配合@class_exc_raiser使用：
        在被@class_exc_raiser装饰的类，需要使用@classmethod_exc_wrapper替换@classmethod
    """

    def inner(cls, *args, **kwargs):
        return func(cls, *args, **kwargs)

    return inner


# 测试代码-------------------------------------
#
# @class_exc_raiser()
# class F():
#     A = 123
#
#     @classmethod_exc_wrapper
#     def t_c(cls, *args, **kwargs):
#         return cls.A
#
#     def t(self, *args, **kwargs):
#         return self.A
#
#     @staticmethod
#     def t_s():
#         return "############"
#
#
# class Son(F):
#     A = 666
#     pass
#
#
# print(F.t_c())
# print(F().t_c())
# print(Son.t_c())
# print(Son().t_c())
#
# print("*************************")
# print(F().t())
# print(Son().t())
#
# print("*************************")
# print(F.t_s())
# print(F().t_s())
# print(Son.t_s())
# print(Son().t_s())
#
# try:
#     1 / 0
# except Exception as e:
#     print(getattr(e, "__str__", None))
