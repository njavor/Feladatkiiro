def ToPrint(nyelv):
	with open("input.txt","r",encoding="utf8") as f:
		with open("output.txt", "a", encoding="utf8") as g:
			if nyelv == "p":
				for sor in f:				
					s = sor.replace("\n", "")
					s= s.replace("\t", " ")
					print(f"print(\"{s}\")")
					g.write(f"print(\"{s}\")\n")
				g.close
			elif nyelv == "cs":
				for sor in f:				
					s = sor.replace("\n", "")
					s = s.replace("\t", " ")
					print(f"Console.WriteLine(\"{s}\")")
					g.write(f"Console.WriteLine(\"{s}\")\n")
				g.close

ToPrint(input("Milyen nyelven szeretnéd a kiírást (\"cs\", \"p\"):   "))
