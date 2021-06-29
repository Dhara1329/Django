from django.shortcuts import render

# Create your views here.

studentDetails = [{'Name':"PARIKH DHARA",
				  'Password':"dhara1234",
				  'Institute':"Faculty of Computer Application & Information Technology",
				  'program':"Integrated Master of Science (IT)",
				  'semester':"IV",
				  'seat':201801619010072,
				  'enroll':201801619010072,
				  'sub1': {'python':[89,"O+"]},
				  'sub2': {'AI':[85,"O+"]},
				  'sub3': {'SE':[83,"O"]},
				  'obtained':257,
				  'total':300
				 },
				 {'Name':"SHAH PRAPTI",
				  'Password':"prapti1234",
				  'Institute':"Faculty of Computer Application & Information Technology",
				  'program':"Integrated Master of Science (IT)",
				  'semester':"IV",
				  'seat':201801619010087,
				  'enroll':201801619010087,
				  'sub1': {'python':[85,"O+"]},
				  'sub2': {'AI':[88,"O+"]},
				  'sub3': {'SE':[89,"O+"]},
				  'obtained':262,
				  'total':300
				 },
				 {'Name':"SHAH JAKSHI",
				  'Password':"jakshi1234",
				  'Institute':"Faculty of Computer Application & Information Technology",
				  'program':"Integrated Master of Science (IT)",
				  'semester':"IV",
				  'seat':201801619010085,
				  'enroll':201801619010085,
				  'sub1': {'python':[88,"O+"]},
				  'sub2': {'AI':[86,"O+"]},
				  'sub3': {'SE':[81,"O"]},
				  'obtained':255,
				  'total':300
				 },
				 {'Name':"JOSHI PRESHITA",
				  'Password':"preshita1234",
				  'Institute':"Faculty of Computer Application & Information Technology",
				  'program':"Integrated Master of Science (IT)",
				  'semester':"IV",
				  'seat':201801619010061,
				  'enroll':201801619010061,
				  'sub1': {'python':[95,"O+"]},
				  'sub2': {'AI':[92,"O+"]},
				  'sub3': {'SE':[90,"O+"]},
				  'obtained':277,
				  'total':300
				 }
				 ]

def homepage(Request):
	return render(Request,"home.html")

def mymarks(Request):
	erollno= int(Request.GET['roll'])
	epass=Request.GET['upass']

	for i in studentDetails:
		if i['enroll']== erollno and i['Password']== epass:
			return render(Request,"Mymarks.html",i)
	return render(Request,"home.html")