N = int(input())

result = []
for n in range(1, N + 1):
    text_n = str(n)
    clap_cnt = text_n.count('3') + text_n.count('6') + text_n.count('9')
    
    if clap_cnt > 0:
        result.append('-' * clap_cnt)
    else:
        result.append(text_n)

print(*result)
