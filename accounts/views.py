from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Realtor,Listings
from listings.models import Listing
from contacts.models import Contact
from realtors.models import Realtor as Realtor1
from listings.choice import state_choices


def register(request):
	if request.method == "POST":
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		phone=request.POST['phone']
		description=request.POST['description']
		photo=request.FILES['photo']
		password=request.POST['password']
		password2=request.POST['password2']

		if password==password2:
			if len(password) >= 6:
				if User.objects.filter(email=email).exists():
					messages.error(request,"Email already registered")
					return redirect('register')
				else:
					realtor = Realtor.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
					realtor.save()
					user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
					user.save()
					realtor1 = Realtor1.objects.create(name=first_name+" "+last_name,photo=photo,description=description,phone=phone,email=email)
					realtor1.save()
					messages.success(request,"You are now registered and can now login")
					return redirect('login')
			else:
				messages.error(request,"Too short Password")
				return redirect('register')
		else:
			messages.error(request,"Password do not match")
			return redirect('register')

	else:
		return render(request,'register.html')	


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html')

def dashboard(request):
	user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
	realtor=Realtor1.objects.all()
	realtor_instance=Realtor1.objects.get(name=request.user.first_name+" "+request.user.last_name)	
	
	
	if request.method=='POST':
		realtor=realtor_instance
		address=request.POST['address']
		city=request.POST['city']
		state=request.POST['state']
		zipcode=request.POST['zipcode']
		description=request.POST['description']
		price=request.POST['price']
		bedrooms=request.POST['bedrooms']
		bathrooms=request.POST['bathrooms']
		garage=request.POST['garage']
		sqft=request.POST['sqft']
		lot_size=request.POST['lot_size']
		photo_main=request.FILES['photo_main']
		photo_1=request.FILES['photo_1']
		photo_2=request.FILES['photo_2']
		photo_3=request.FILES['photo_3']
		photo_4=request.FILES['photo_4']
		photo_5=request.FILES['photo_5']
		photo_6=request.FILES['photo_6']
		list_date=request.POST['list_date']
		listing1 = Listing.objects.create(realtor=realtor_instance,address=address,city=city,state=state,zipcode=zipcode,description=description,price=price,bedrooms=bedrooms
			,bathrooms=bathrooms,garage=garage,sqft=sqft,lot_size=lot_size,photo_main=photo_main,photo_1=photo_1,photo_2=photo_2,
			photo_3=photo_3,photo_4=photo_4,photo_5=photo_5,photo_6=photo_6,list_date=list_date)
		listing1.save()
		listings123=Listing.objects.all().filter(realtor=realtor_instance)
		return render(request,'dashboard.html',{
				'contacts': user_contacts,
				'listings':listings123
			})
	else:
		listings123=Listing.objects.all().filter(realtor=realtor_instance)
		return render(request,'dashboard.html',{
			'contacts': user_contacts,
			'listings':listings123
			})
def logout(request):
	if request.method=='POST':
		auth.logout(request)
		messages.success(request,"Now you are successfully logout")
		return redirect('index')

def postad(request):
	locations=["1st block jayanagar", "1st phase jp nagar", "2nd phase judicial layout", "2nd stage nagarbhavi", "5th block hbr layout", "5th phase jp nagar", "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar", "9th phase jp nagar", "aecs layout", "abbigere", "akshaya nagar", "ambalipura", "ambedkar nagar", "amruthahalli", "anandapura", "ananth nagar", "anekal", "anjanapura", "ardendale", "arekere", "attibele", "beml layout", "btm 2nd stage", "btm layout", "babusapalaya", "badavala nagar", "balagere", "banashankari", "banashankari stage ii", "banashankari stage iii", "banashankari stage v", "banashankari stage vi", "banaswadi", "banjara layout", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", "battarahalli", "begur", "begur road", "bellandur", "benson town", "bharathi nagar", "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli", "bommasandra", "bommasandra industrial area", "bommenahalli", "brookefield", "budigere", "cv raman nagar", "chamrajpet", "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar", "chikkalasandra", "choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura", "dasarahalli", "devanahalli", "devarachikkanahalli", "dodda nekkundi", "doddaballapur", "doddakallasandra", "doddathoguru", "domlur", "dommasandra", "epip zone", "electronic city", "electronic city phase ii", "electronics city phase 1", "frazer town", "gm palaya", "garudachar palya", "giri nagar", "gollarapalya hosahalli", "gottigere", "green glen layout", "gubbalala", "gunjur", "hal 2nd stage", "hbr layout", "hrbr layout", "hsr layout", "haralur road", "harlur", "hebbal", "hebbal kempapura", "hegde nagar", "hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", "hosakerehalli", "hoskote", "hosur road", "hulimavu", "isro layout", "itpl", "iblur village", "indira nagar", "jp nagar", "jakkur", "jalahalli", "jalahalli east", "jigani", "judicial layout", "kr puram", "kadubeesanahalli", "kadugodi", "kaggadasapura", "kaggalipura", "kaikondrahalli", "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", "kanakapura", "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli", "kasturi nagar", "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town", "kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", "kodihalli", "kogilu", "konanakunte", "koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate", "kumaraswami layout", "kundalahalli", "lb shastri nagar", "laggere", "lakshminarayana pura", "lingadheeranahalli", "magadi road", "mahadevpura", "mahalakshmi layout", "mallasandra", "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "marsur", "mico layout", "munnekollal", "murugeshpalya", "mysore road", "ngr layout", "nri layout", "nagarbhavi", "nagasandra", "nagavara", "nagavarapalya", "narayanapura", "neeladri nagar", "nehru nagar", "ombr layout", "old airport road", "old madras road", "padmanabhanagar", "pai layout", "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout", "prithvi layout", "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", "rajiv nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar", "sanjay nagar", "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", "sector 2 hsr layout", "sector 7 hsr layout", "seegehalli", "shampura", "shivaji nagar", "singasandra", "somasundara palya", "sompura", "sonnenahalli", "subramanyapura", "sultan palaya", "tc palaya", "talaghattapura", "thanisandra", "thigalarapalya", "thubarahalli", "thyagaraja nagar", "tindlu", "tumkur road", "ulsoor", "uttarahalli", "varthur", "varthur road", "vasanthapura", "vidyaranyapura", "vijayanagar", "vishveshwarya layout", "vishwapriya layout", "vittasandra", "whitefield", "yelachenahalli", "yelahanka", "yelahanka new town", "yelenahalli", "yeshwanthpur"]

	return render(request,'postad.html',{
		'locations':locations,
		'state_choices':state_choices
		})	

def delete(request,list_id):
	instance = Contact.objects.get(id=list_id)
	instance.delete()
	user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
	realtor=Realtor1.objects.all()
	realtor_instance=Realtor1.objects.get(name=request.user.first_name+" "+request.user.last_name)	
	listings123=Listing.objects.all().filter(realtor=realtor_instance)
	return render(request,'dashboard.html',{
				'contacts': user_contacts,
				'listings':listings123
			})