from django.contrib import admin
from .models import Question, Choice

# Register your models here.

#class ChoiceInline(admin.StackedInline): #카드형식으로 나열
class ChoiceInline(admin.TabularInline): #테이블 형식
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']  #필드 순서 변경
    fieldsets = [
        ('Question Statement',
         {'fields':
              ['question_text']
          }),
        ('Date Information',
         {'fields':
              ['pub_date'],
          'classes':
              ['collapse']
          }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')    #레코드 리스트 컬럼 지정
    list_filter = ['pub_date']  #필터 사이드 바 추가
    search_fields = ['question_text']   #검색 박스 추가
    list_per_page = 4   #페이지네이션 튜플 개수 설정

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)