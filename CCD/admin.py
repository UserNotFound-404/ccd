from django.contrib import admin
from django.contrib.admin import ModelAdmin

from CCD.models import NewsMonitoring


class NewsMonitoringList(ModelAdmin):
    list_display = ("id", "date", "short_description", "area_tag", "topic_tag", "link", "source", "source_tag", "subject",
                    "additional_info", "type_of_threat", "evaluation", "grand_narrative", "narrative", "status",
                    "suggestions_for_response", "country", "ua_region", "index")


admin.site.register(NewsMonitoring, NewsMonitoringList)