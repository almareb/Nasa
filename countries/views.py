from django.shortcuts import render
from .models import CountryPollution
def home_view(request):
	qs = CountryPollution.objects.all()
	title_query = request.GET.get('countryResult')
	
	if title_query != '' and title_query is not None:
		qs =qs.filter(title__icontains=title_query)
	context = {
		'queryset':qs
	}
	print(context)

	return render(request,'countries/index.html',context)


