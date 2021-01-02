

def blacklist(func):
    def wrapper(*args, **kwargs):
        from AppiumStudy.frame.pages.basepage import BasePage
        instance: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance.error_num = 0
            return result
        except Exception as e:
            if instance.error_num > instance.max_num:     # 判断是否超过最大查找次数
                raise e
            instance.error_num += 1            # 查找次数加1
            for black_ele in instance.black_list:                  # 从黑名单中遍历元素，依次进行处理
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    return wrapper(*args,**kwargs)          # 处理完黑名单后，再次查找原来的元素
            raise e
    return wrapper

