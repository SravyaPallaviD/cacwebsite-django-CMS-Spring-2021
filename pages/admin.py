from django.contrib import admin
from .models import Statistics
<<<<<<< HEAD
from .models import Image1
from .models import Image2
from .models import Image3
from .models import Statisticscannon
from .models import Team, ExecutiveCommittee, BoardMember, Event, EventTopImage, PressRelease, NewsLetter, Resource, Link

# Register your models here.

admin.site.register(Statistics)
admin.site.register(Image1)
admin.site.register(Image2)
admin.site.register(Image3)
=======
from .models import SlideshowImages
#from .models import Image2
#from .models import Image3
from .models import Statisticscannon
from .models import Team, ExecutiveCommittee, BoardMember, Event, EventTopImage, PressRelease, NewsLetter, RutherfordService, CannonService, MediaInformation
from .models import DarknesstoLight,Imagesond2l, PostImage, GratitudeCards
# Register your models here.

admin.site.register(Statistics)
admin.site.register(SlideshowImages)
#admin.site.register(Image2)
#admin.site.register(Image3)
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
admin.site.register(Statisticscannon)
admin.site.register(Team)
admin.site.register(ExecutiveCommittee)
admin.site.register(BoardMember)
admin.site.register(Event)
admin.site.register(EventTopImage)
admin.site.register(PressRelease)
admin.site.register(NewsLetter)
<<<<<<< HEAD
admin.site.register(Resource)
admin.site.register(Link)


#class PostImageAdmin(admin.StackedInline):
#	model = PostImage

#@admin.register(GratitudeCards)
#class PostAdmin(admin.ModelAdmin):
#	inlines = [PostImageAdmin]
#
#	class Meta:
#		model = GratitudeCards

#@admin.register(PostImage)
#class PostImageAdmin(admin.ModelAdmin):
#	pass
=======
admin.site.register(RutherfordService)
admin.site.register(CannonService)
admin.site.register(MediaInformation)
admin.site.register(DarknesstoLight)
admin.site.register(Imagesond2l)

class PostImageAdmin(admin.StackedInline):
	model = PostImage

@admin.register(GratitudeCards)
class PostAdmin(admin.ModelAdmin):
	inlines = [PostImageAdmin]

	class Meta:
		model = GratitudeCards

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
	pass
>>>>>>> 18140e79ee359a5792e322ec4efb24b84de933b3
