import numpy as np
import pandas as pd
import os
from os import walk

class wikihow:
	def __init__(self):
		self.df = pd.read_csv('final.csv')
		
	def print_doc(self,n=0):
		print(self.df['Summary'][n])
		print("\n======================================\n")
		print(self.df['Text'][n])
		
	def preprocess_summary(self,summ):
		summ_splits = summ.split("\r\n")
		new_summ = []
		for l in summ_splits:
			if l != '' and not l.isspace():
				new_summ.append(l.strip(', '))
		return new_summ
		
	def prepare_dataset(self):
		ex = 0
		for index, row in df.iterrows():
			if index < 0:
				continue
			fn = "dataset/d_"+str(index)+".story"
			try:
				f = open(fn, "w", encoding='utf8')
				if type(row["Summary"]) != str or type(row["Text"]) != str:
					continue
				summ = self.preprocess_summary(row['Summary'])
				text = self.preprocess_summary(row['Text'])
				for line in text:
					f.write(line+"\n\n")
				for line in summ:
					f.write("@highlight\n\n")
					f.write(line+"\n\n")
				f.close()
			except:
				os.remove(fn)
				ex += 1
				print("Exception occurred! - ",ex)
		self.split_train_val_test()
		
	def split_train_val_test(self,url="dataset"):
		f = []
		for (dirpath, dirnames, filenames) in walk(url):
			f.extend(filenames)
			break
			
		urllists = open("url_lists/all_train.txt", "w")
		for file in f[0:200000]:
			urllists.write(file+"\n")
		urllists.close()
		urllists = open("url_lists/all_val.txt", "w")
		for file in f[200000:250000]:
			urllists.write(file+"\n")
		urllists.close()
		urllists = open("url_lists/all_test.txt", "w")
		for file in f[250000:len(f)]:
			urllists.write(file+"\n")
		urllists.close()