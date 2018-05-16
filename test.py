#!/usr/bin/python
#coding:utf-8



# re_string = raw_input("1.(A)輸入字串:")
# print re_string[::-1]

# re_words_string = raw_input("2.(B)輸入句子:")

# string_list = re_words_string.split()
# output = ""
# for i in string_list:
# 	re_word = i[::-1]
# 	output = output+ re_word + " "
# print output.strip()


num  = int(input("2.輸入數字:"))

count = 0
for i in range(num):
	if (i+1)/3 != 0 and (i+1)/5 != 0 :
		count +=1
print count
