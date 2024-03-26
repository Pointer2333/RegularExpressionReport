import random

def generate_mixed_ipv4():
    ipv4_list = []
    for _ in range(100):
        # 生成一个随机的字符串，部分内容为有效的 IPv4 地址
        ipv4 = f"{random.randint(0, 500)}.{random.randint(0, 500)}.{random.randint(0, 500)}.{random.randint(0, 500)}"
        ipv4_list.append(ipv4)

    return ipv4_list

def main():
    ipv4_strings = generate_mixed_ipv4()

    # 将生成的字符串写入到文件中
    with open("ipv4_strings.txt", "w") as file:
        for ipv4 in ipv4_strings:
            file.write(ipv4 + "\n")

    print("100条格式为XXX.XXX.XXX.XXX的字符串已生成并保存到ipv4_strings.txt文件中。")

if __name__ == "__main__":
    main()
