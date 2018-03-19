#-*- coding: utf-8 -*-
import sys


result = ""
chat = False
with open("a.txt", 'rt', encoding='UTF8') as f:
	for line in f:
		try:
			line = line.strip()
			
			str1 = "Record Number     :"
			if str1 in line:
				result = ""
				value = line.split(str1)[1].strip()
				result += '"'+value+'",'
				continue
				
			str1 = "Action Type       :"
			if str1 in line:
				value = line.split(str1)[1].strip()
				result += '"'+value+'",'
				continue
				
			str1 = "Action Time       :"
			if str1 in line:
				value = line.split(str1)[1].strip()
				result += '"'+value+'",'
				continue
				
			str1 = "End Time          :"
			if str1 in line:
				value = line.split(str1)[1].strip()
				result += '"'+value+'",'
				continue
			
			str1 = "User Name         :"
			if str1 in line:
				value = line.split(str1)[1].strip()
				result += '"'+value+'",'
				continue
				
			str1 = "Display Name      :"
			if str1 in line:
				value = line.split(str1)[1].strip()
				result += '"'+value+'",'
				continue
				
			str1 = "Duration          :"
			if str1 in line:
				value = line.split(str1)[1].strip()
				result += '"'+value+'",'
				continue
				
			str1 = "Chat Message      :"
			if str1 in line:
				value = line.split(str1)[1]
				value = value.replace('"', '')
				value = value.replace(',', '.')
				result += '"'+value
				chat = True
				continue
				
			str1 = "ChatID            :"
			if str1 in line:
				value = line.split(str1)[1].strip()
				result += '","'+value+'",'
				chat = False
				continue
			elif chat:
				result += line+'\n'
				continue
				
			str1 = "Filename          :"
			if str1 in line:
				value = line.split(str1)[1].strip()
				result += '"'+value+'"'
				print(result)
				result=""
				continue
		except:
			print("error")
