from django.shortcuts import render

posts = [
	{
		'author': 'VeerSK',
		'title': 'Blog Post 1',
		'content': 'Post Content 1',
		'date_posted': 'July 27, 2019'
	},
	{
		'author': 'MansiB',
		'title': 'Blog Post 2',
		'content': 'Post Content 2',
		'date_posted': 'July 28, 2019'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, ('blog/home.html'), context)

def about(request):
	return render(request, ('blog/about.html'), {'title': 'About'})