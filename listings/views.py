from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Band,Listing
from .forms import ContactUsForm,BandForm,ListingsForm
from django.core.mail import send_mail

def band_list(request):
    bands=Band.objects.all()
    #select * from Band
    return render(request,'listings/band_list.html',{'bands':bands})

def about (request):
    return render(request,'listings/about.html')

def listings_list(request):
    annonces=Listing.objects.all()
    #Select * from Listing
    return render(request,'listings/listings_list.html',{'annonces':annonces})

def contact(request):
    if request.method=='POST':
        #creer une instance de notre fromulaire et le remplir avec les donnees POST
        #request.post contient les donnees 
        form=ContactUsForm(request.POST)
        #si tous les champs de notre fromulaire contiennent des donees valides
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else :
        #Ceci doit etre une requete GET, donc creer un formulaire vide
        form=ContactUsForm()
    return render(request,'listings/contact.html',{'form':form})

def band_detail(request,id):
    bands=Band.objects.get(id=id)
    #select * from Band where id=id
    return render(request, 'listings/band_detail.html',{'bands':bands})

def listings_detail(request,id):
    listings=Listing.objects.get(id=id)
    #select * from Listings where id=id
    return render(request, 'listings/listings_detail.html',{'listings':listings})

def email_sent(request):
    return render(request,'listings/email_sent.html')

def band_create(request):
    if request.method=='POST':
        form= BandForm(request.POST)
        if form.is_valid():
            #creer une nouvelle "band" et la sauvegarder dans la db
            band=form.save()
            #rediriger vers la page de detail du groupe que nous venons de creer
            return redirect('band-detail',band.id)
    else :
        form=BandForm()
    return render(request,'listings/band_create.html',{'form':form})
def listings_create(request):
    if request.method=='POST':
        form=ListingsForm(request.POST)
        if form.is_valid():
            Listings=form.save()
            return redirect('listings-detail',Listings.id)
    else:
        form=ListingsForm()
    return render(request,'listings/listings_create.html',{'form':form})

def band_update(request,id):
    band=Band.objects.get(id=id)
    if request.method=='POST':
        form=BandForm(request.POST,instance=band)
        if form.is_valid():
            band=form.save()
            return redirect('band-list')
    else:
        form=BandForm(instance=band)
    return render(request,'listings/band_update.html',{'form':form})

def listings_update(request,id):
    listing=Listing.objects.get(id=id)
    if request.method=='POST':
        form=ListingsForm(request.POST,instance=listing)
        if form.is_valid():
            listing=form.save()
            return redirect('listing-list')
    else:
        form=ListingsForm(instance=listing)
        return render(request,'listings/listings_create.html',{'form':form})
    
def band_delete(request,id):
    band=Band.objects.get(id=id)
    if request.method=="POST":
        band.delete()
        return redirect('band-list')
    return render(request,'listings/band_delete.html',{'band':band})
def listings_delete(request,id):
    listing=Listing.objects.get(id=id)
    if request.method=="POST":
        listing.delete()
        return redirect('listings-list')
    return render(request,'listings/listings_delete.html',{'listing':listing})