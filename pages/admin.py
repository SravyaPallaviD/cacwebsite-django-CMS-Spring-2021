from django.contrib import admin
from .models import Statistics
from .models import Image1
from .models import Image2
from .models import Image3
from .models import Statisticscannon
from .models import Team, ExecutiveCommittee, BoardMember, Event, EventTopImage, PressRelease, NewsLetter
# Register your models here.

admin.site.register(Statistics)
admin.site.register(Image1)
admin.site.register(Image2)
admin.site.register(Image3)
admin.site.register(Statisticscannon)
admin.site.register(Team)
admin.site.register(ExecutiveCommittee)
admin.site.register(BoardMember)
admin.site.register(Event)
admin.site.register(EventTopImage)
admin.site.register(PressRelease)
admin.site.register(NewsLetter)

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
