def ToPrint():
	with open("input.txt","r",encoding="utf8") as f:
		with open("output.txt", "a", encoding="utf8") as g:
			for sor in f:
				s = sor.replace("\n", "")
				s= s.replace("\t", " ")
				print(f"print(\"{s}\")")
				g.write(f"print(\"{s}\")\n")
			g.close

ToPrint()