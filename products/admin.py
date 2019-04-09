from django.contrib import admin
import nested_admin
from products.models import (
    Category,
    Content,
    Product,
    Image,
    File,
    Lecture,
    Video,
    Product,
    Appraisal,
    ReplyChapter
)

class ReplyChapterAdmin(nested_admin.NestedModelAdmin):
    list_display = ('pk', 'video', 'user', 'order', 'created_at', 'updated_at')

class ImageAdmin(nested_admin.NestedModelAdmin):  # 테이블 형식
    fieldsets = [
        ('샘플이미지', {'fields':
            [
                'image',
                'description',
            ]}),
    ]
    list_display = ('image',  'pk', 'description',)


class FileAdmin(nested_admin.NestedModelAdmin):  # 테이블 형식
    fieldsets = [
        ('컨텐츠파일', {'fields':
            [
                'file',
                'type',
                'description',
            ]}),
    ]
    list_display = ('description', 'type', 'file',  'pk', )

class CategoryAdmin(admin.ModelAdmin):
    fields = ['title',
              'section',
              'slug',
              'description']
    list_display= ['pk',
                   'title',
                   'section',
                   'slug',
                   'description']
    prepopulated_fields = {'slug': ('title',)}

class VideoInline(nested_admin.NestedStackedInline):  # 테이블 형식

    extra = 1
    model = Video

class VideoAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        ('비디오정보', {'fields':
            [
                'title',
                'video_link',
                'introduce',
            ]}),
    ]

    list_display = ('title', 'get_introduce', 'pk', 'video_link',)

    def get_introduce(self, obj):
        return str(obj.introduce)[0:30]


class LectureInline(nested_admin.NestedStackedInline):  # 테이블 형식
    model = Lecture
    extra = 1
    max_num = 1
    inlines = [VideoInline]

class LectureAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        ('강좌정보', {'fields':
            [
                'introduce',

            ]}),
        ('추가정보', {
            'classes': ('collapse',),
            'fields':
                [
                    'teacher',
                    'location',

                ]}),
        ('기간정보', {
            'classes': ('collapse',),
            'fields':
                [
                    'register_from',
                    'period_from',
                    'period_to',
                    'duration',
                ]}),

    ]
    #
    list_display = ('get_introduce', 'pk', 'register_from',)

    def get_introduce(self, obj):
        return str(obj.introduce)[0:30]



class ProductInline(nested_admin.NestedTabularInline):  # 테이블 형식

    model = Product
    extra = 1
    max_num = 1

class ProductAdmin(nested_admin.NestedModelAdmin):
    fields = ['introduce', 'link', 'stock']
    list_display = ('get_title', 'get_category', 'link', 'stock')
    list_editable = ['stock']

    def get_introduce(self, obj):
        return str(obj.introduce)[0:30]

    def get_title(self, obj):
        return str(obj.content.title)

    def get_category(self, obj):
        return str(obj.content.category)


class ContentAdmin(nested_admin.NestedModelAdmin):
    # fields = ['pub_date', 'question_text']  #필드 순서 변경

    fieldsets = [
        ('콘텐츠 기본 정보', {
            'fields':
            [
                'category',
                'title',
                'slug',
                'description',
                'related_content',
                'sample',
            ]}),

        ('판매정보', {
            'classes': ('collapse',),
            'fields':
            [
                'cost',
                'discount',
                'isSale',
                'isShow',
                'isDiscount',
                'recommend',
            ]}),
        ('추가정보', {
            'classes': ('collapse',),
            'fields':
            [
                'image',
                'file',
            ]}),
    ]
    #inlines = [ProductInline]
    inlines = [LectureInline, ProductInline]
    list_display = ('title',
                    'category',
                   # 'get_section',
                    'recommend',
                    'cost',
                    'isDiscount',
                    'discount',
                    'get_stock',
                    'isShow',
                    'isSale',
                    'slug',
                    'added',
                    'updated',
                    )  # 레코드 리스트 컬럼 지정
    list_editable = ['cost', 'isSale', 'isDiscount', 'discount','isShow', 'recommend',]
    search_fields = ['title', 'description']  # 검색 박스 추가
    list_per_page = 10  # 페이지네이션 튜플 개수 설정
    prepopulated_fields = {'slug': ('title',)}

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):


            try:
                print(str(obj.category.section))
                print(str(inline.__class__.__name__))
                if obj.category.section == '강좌' and inline.__class__.__name__ == 'LectureInline':
                    yield inline.get_formset(request, obj), inline
                if obj.category.section == '상품' and inline.__class__.__name__ == 'ProductInline':
                    yield inline.get_formset(request, obj), inline
            except:
                pass



    def get_section(self, obj):
        return str(obj.category.section)

    def get_stock(self, obj):
        if obj.category.section == '상품':
            try:
                #print(obj.product_set.first().__dir__())
                if hasattr(obj.product_set.first(), 'stock'):
                    print(obj.product_set.first().stock)
                    return obj.product_set.first().stock
                else:
                    return '미완료'
            except:
                return '미완료'

        else:
            return '해당없음'


admin.site.register(Content, ContentAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Appraisal)
admin.site.register(ReplyChapter, ReplyChapterAdmin)
