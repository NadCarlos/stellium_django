from typing import List, Optional

from shop.models import SelectionTimes


class SelectionTimesRepository:

    def get_all(self) -> List[SelectionTimes]:
        return SelectionTimes.objects.all()
    
    def filter_by_time(self) -> Optional[SelectionTimes]:
        return SelectionTimes.objects.values_list("time", flat=True)