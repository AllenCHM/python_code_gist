# coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# json.loads()是将str转化成dict格式，json.dumps()是将dict转化成str格式。
# json.load()和json.dump()也是类似的功能，只是与文件操作结合起来了。

# 解码
import json

with open('build_info.json', 'r') as f:
    array = json.load(f)
print(array)

# 在编码JSON的时候，还有一些选项很有用。
#  如果你想获得漂亮的格式化字符串后输出，可以使用 json.dumps() 的indent参数。 它会使得输出和pprint() 函数效果类似：

data = {"price": 542.23, "name": "ACME", "shares": 100}
print(json.dumps(data))
print(json.dumps(data, indent=4))

# {
#     "price": 542.23,
#     "name": "ACME",
#     "shares": 100
# }


# 保存为 json 文件：
# 编码
import json

a = {"name": "michael"}
with open("demo.json", "w") as f:
    json.dump(a, f, indent=4)
