# pig latin translater 

while True:
	word = raw_input("Enter a word: ")
	if word == "exit":
		break

vowels = "aeiouy"

slice_pos = 0
for i in range(len(word)):
	if word[i] in vowels:
		slice_pos = i
		break
		
print word [slice_pos: ] + word[:slice_pos] + "aye"
