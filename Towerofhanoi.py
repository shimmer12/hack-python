

def TowH(n , source, destination, auxiliary):
	if n==1:
		print ("Move discs 1 from source",source,"to destination",destination)
		return
	TowH(n-1, source, auxiliary, destination)
	print ("Move discs",n,"from source",source,"to destination",destination)
	TowH(n-1, auxiliary, destination, source)
		

n = 4
TowH(n,'A','B','C')



