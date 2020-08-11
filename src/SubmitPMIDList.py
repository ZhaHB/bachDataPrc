import requests
import io
import json
import sys


def SubmitPMIDList(Inputfile,Format,Bioconcept):
	
	json = {}
	#
	# load pmids
	#

	nothing_to_return = []
	with io.open(Inputfile, 'r', encoding="utf-8") as file_input:

		for pmid in file_input.readlines():

			pmid = pmid.replace("\n", "")
			json = {"pmids": [pmid]}

			#
			# load bioconcepts
			#
			if Bioconcept != "":
				json["concepts"] = Bioconcept.split(",")

			#
			# request
			#
			r = requests.post("https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/"+Format , json = json)

			if r.status_code != 200 :
				print("[Error]: HTTP code " + str(r.status_code))

			elif len(r.text) == 0:
				with open(str(kwd) + "_nothting_to_write.txt", "a+", encoding="utf-8")as wfile1:
					wfile1.write(pmid+"\n")

			with open(str(kwd)+"_pubtator.txt", 'a+', encoding="utf-8")as wfile:
				wfile.write(r.text)

	# return nothing_to_return


if __name__ == "__main__":

	"""
	arg_count=0
	for arg in sys.argv:
		arg_count+=1
	if arg_count<2 or (sys.argv[2]!= "pubtator" and sys.argv[2]!= "biocxml" and sys.argv[2]!= "biocjson"):
		print("\npython SubmitPMIDList.py [InputFile] [Format] [BioConcept]\n\n")
		print("\t[Inputfile]: a file with a pmid list\n")
		print("\t[Format]: pubtator (PubTator), biocxml (BioC-XML), and biocjson (JSON-XML)\n")
		print("\t[Bioconcept]: gene, disease, chemical, species, proteinmutation, dnamutation, snp, and cellline. Default includes all.\n")
		print("\t* All input are case sensitive.\n\n")
		print("Eg., python SubmitPMIDList.py examples/ex.pmid pubtator gene,disease\n\n")
	else:
		Inputfile = sys.argv[1]
		Format = sys.argv[2]
		Bioconcept=""
		if arg_count>=4:
			Bioconcept = sys.argv[3]
	"""

	keyword = ["neurobiology"]

	Format = "pubtator"

	Bioconcept=""

	for kwd in keyword:

		Inputfile = str(kwd) + "_ex.pmid"
		SubmitPMIDList(Inputfile, Format, Bioconcept)
