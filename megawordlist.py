import time

word = R"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

with open("megalist.txt","w") as mega:
	for a in word:
		for b in word:
			for c in word:
				for d in word:
					for f in word:
						for g in word:
							for h in word:
								for e in word:
									for s in word:
										for g in word:
											print(f"\r{a}{b}{c}{d}{f}{g}{h}{e}{s}{g}",end="")
											mega.write(f"{a}{b}{c}{d}{f}{g}{h}{e}{s}{g}\n")

#Length : 9
#Include Characters : 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
#File Size : 95*5 Zettabytes
