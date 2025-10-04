# cnt = {}
# total = 0
# with open('book.txt','r') as f:
#     content = f.read()
#     for i in content:
#         if ord(i) > 120000:
#             cnt[i] = cnt.get(i,0) + 1
#             total+=1
# for i in cnt:
#     cnt[i] = round(cnt[i]/total*100,3)
# print(cnt)

ref = {'🥺': 'S', '🤡': 'T', '😙': 'A', '😍': 'E', '🙀': 'L', '🤐': 'Y', '😵': 'P', '👧': 'U', '😡': 'M', '🤪': 'B', '😎': 'C', '😂': 'K', '👂': 'I', '🤩': 'G', '🥴': 'N', '😃': 'F', '😉': 'R', '🥶': 'O', '😢': 'H', '🥳': 'D', '🙄': 'W', '🤓': 'Z', '😒': 'J', '🦣': 'V', '👌': 'Q', '🫠': 'X'}
res = ''
total = 0
with open('book.txt','r') as f:
    content = f.read()
    for i in content:
        res += ref.get(i,i)

with open('res.txt','w') as f:
    f.write(res)
