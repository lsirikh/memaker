# from django.contrib import admin
# from lectures.models import Section, Category, Lecture, Video
#
# # Register your models here.
# #class ChoiceInline(admin.StackedInline): #카드형식으로 나열
# class DetailInline(admin.TabularInline): #테이블 형식
#     model = Video
#     extra = 1
#
# class LectureAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Lecture Information', {'fields':
#                                      ['section',
#                                       'category',
#                                       'title',
#                                       'description',
#                                       'content'
#                                       ]}),
#         ('Lecture Fee Info', {'fields':
#                                      ['fee',
#                                       'discount',
#                                       'isDiscount'
#                                       ],
#                              'classes':
#                                     ['collapse']
#                              }),
#         ('Lecture Date Info', {'fields':
#                                      ['register_from',
#                                       'register_to',
#                                       'period_to',
#                                       'period_from'
#                                       ],
#                                'classes':
#                                    ['collapse']
#                                }),
#         ('Lecture Data & Image', {'fields':
#                                       ['sample',
#                                      'lecture_image']}),
#         ('Lecture Status Info', {'fields':
#                                    ['isSale',
#                                     'isShow'
#                                     ]}),
#         ('Lecture Etc Info', {'fields':
#                                    ['teacher',
#                                     'material',
#                                     'location'
#                                     ],
#                                'classes':
#                                    ['collapse']
#                                }),
#     ]
#     inlines = [DetailInline]
#     list_display = ('title', 'section', 'category', 'added', 'updated', 'isSale', 'isShow')
#     list_per_page = 4
#
# admin.site.register(Section)
# admin.site.register(Category)
# admin.site.register(Lecture, LectureAdmin)
# admin.site.register(Video)