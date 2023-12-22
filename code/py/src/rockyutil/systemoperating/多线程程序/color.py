class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# 使用ANSI转义序列打印有颜色的内容
print(bcolors.HEADER + "这是头部内容" + bcolors.ENDC)
print(bcolors.OKBLUE + "这是蓝色的内容" + bcolors.ENDC)
print(bcolors.OKGREEN + "这是绿色的内容" + bcolors.ENDC)
print(bcolors.WARNING + "这是警告的内容" + bcolors.ENDC)
print(bcolors.FAIL + "这是失败的内容" + bcolors.ENDC)
