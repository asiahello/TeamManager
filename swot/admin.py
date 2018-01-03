from django.contrib import admin

# Register your models here.
from swot.models import Factor, PlayerFactor, SwotAnalysis, AnalysisSubCategory


class FactorAdmin(admin.ModelAdmin):
    list_display = ('name', 'analysis_category', 'analysis_subcategory')
    list_filter = ('name', 'analysis_category', 'analysis_subcategory')
    ordering = ['analysis_category', 'analysis_subcategory']
    search_fields = ['name']


class PlayerFactorAdmin(admin.ModelAdmin):
    list_display = ('factor', 'swot_category', 'swot_analysis')
    list_filter = ('factor', 'swot_category', 'swot_analysis')
    search_fields = ['swot_analysis']


class SwotAnalysisAdmin(admin.ModelAdmin):
    list_display = ('owner', 'update_date')
    list_filter = ['owner']
    search_fields = ['owner']


class AnalysisSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Factor, FactorAdmin)
admin.site.register(PlayerFactor, PlayerFactorAdmin)
admin.site.register(SwotAnalysis, SwotAnalysisAdmin)
admin.site.register(AnalysisSubCategory, AnalysisSubCategoryAdmin)
