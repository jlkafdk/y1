import os
import inspect
import importlib


def loader(name):
    """
    动态执行 hook 函数
    """
    # 被调用文件的目录
    stack_t = inspect.stack()
    ins = inspect.getframeinfo(stack_t[1][0])
    file_dir = os.path.dirname(os.path.abspath(ins.filename))
    # 被调用文件目录下面 *_conf.py 文件
    all_hook_files = list(filter(lambda x: x.endswith("_conf.py"), os.listdir(file_dir)))
    all_hook_module = list(map(lambda x: x.replace(".py", ""), all_hook_files))

    # 动态加载 *_config.py
    hooks = []
    for module_name in all_hook_module:
        hooks.append(importlib.import_module(module_name))

    # 根据传过来的 name 函数名，从 *_conf.py 文件查找并执行。
    for per_hook in hooks:
        # 动态执行 process 函数
        func = getattr(per_hook, name)
        return func()
