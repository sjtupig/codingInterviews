def replace_blank(s):
	#python处理字符串很高效
	return s.replace(' ','%20')


s = 'We Are Happy'
print(replace_blank(s))