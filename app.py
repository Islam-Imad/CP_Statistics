from typing import List

import numpy as np
import matplotlib.pyplot as plt


from backend import Platform, PlatformFactory, LeetCode, CodeForces, CodeChef, AtCoder, UVA
PF = PlatformFactory()
platform_list = []
platform_list.append(PF.get_platform("LeetCode"))
platform_list.append(PF.get_platform("CodeForces"))
platform_list.append(PF.get_platform("CodeChef"))
platform_list.append(PF.get_platform("AtCoder"))
platform_list.append(PF.get_platform("UVA"))
platform_list.append(PF.get_platform("SPOJ"))

x = []
y = []
total = 0
for platform in platform_list:
    message = f"please enter your {platform.get_identifier()} in {platform.get_name()} : "
    identifier = input(message).split()[0]
    solved_problems = platform.get_total_solved_problems(identifier)
    # print(identifier)
    print(f"Total solved problems in {platform.get_name()} : {solved_problems}")
    y.append(platform.get_name())
    x.append(solved_problems)
    total += solved_problems

for item in y:
    print(item)

plt.pie(x, labels=y)
plt.legend()
plt.subplot().set_title(str(total), {'fontsize': 30})
plt.show()

