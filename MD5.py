import md5_main
import sys
import six

a = 'e62cdf2ead1ad23a6310662b0c9a8dee'#ZhangQimeng的Hash值
length = 11
b = '202000460118'

s1 = eval('0x' + a[:8].encode('utf-8')[::-1].decode('utf-8'))
s2 = eval('0x' + a[8:16].encode('utf-8')[::-1].decode('utf-8'))
s3 = eval('0x' + a[16:24].encode('utf-8')[::-1].decode('utf-8'))
s4 = eval('0x' + a[24:32].encode('utf-8')[::-1].decode('utf-8'))

print(s1,s2,s3,s4)

jiashe = "a" * length
test = jiashe + '\x80' + '\x00'* 44 + str(six.int2byte(length*8)) + '\x00\x00\x00\x00\x00\x00\x00' + b

s = md5_main.deal_rawInputMsg(b)
r = md5_main.deal_rawInputMsg(jiashe)
inp = s[len(r):]

print('填充完的数据为:' + test + '\n')
print('扩充完的数据为(16进制):' + s)
print('截取最后分组的数据(16进制):' + inp)
print("填充后的md5为:" + md5_main.run_md5(s1,s2,s3,s4,inp))
