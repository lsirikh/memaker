from django.contrib import admin
from products.models import Category, Product, Detail

# Register your models here.

#class ChoiceInline(admin.StackedInline): #카드형식으로 나열
class DetailInline(admin.TabularInline): #테이블 형식
    model = Detail
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']  #필드 순서 변경
    fieldsets = [
        ('Product Information', {'fields':
                                     ['title',
                                     # 'added',
                                     # 'updated',
                                      'cost',
                                      'discount',
                                      'isSale',
                                      'description',
                                      'category']}),
        ('Data & Image', {'fields': ['file',
                                     'movie',
                                     'product_image',
                                     'related_lec']}),
    ]
    inlines = [DetailInline]
    list_display = ('title', 'added', 'updated', 'category', 'isSale', 'product_image', 'file')    #레코드 리스트 컬럼 지정
    search_fields = ['description']   #검색 박스 추가
    list_per_page = 4   #페이지네이션 튜플 개수 설정






admin.site.register(Product, ProductAdmin)
admin.site.register(Detail)
admin.site.register(Category)
