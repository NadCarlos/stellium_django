from typing import List, Optional

from shop.models import SelectionTimes


class SelectionTimesRepository:

    def get_all(self) -> List[SelectionTimes]:
        return SelectionTimes.objects.all()