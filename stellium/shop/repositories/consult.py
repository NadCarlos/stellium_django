from typing import List, Optional

from shop.models import Consult


class ConsultRepository:

    def get_all(self) -> List[Consult]:
        return Consult.objects.all()
    
    def filter_by_id(self, id) -> Optional[Consult]:
        return Consult.objects.filter(id=id).first()
    
    def filter_by_date(self) -> Optional[Consult]:
        return Consult.objects.values_list("date", "time", flat=False)
    
    def create(
        self,
        date: str,
        time: str,
    ):
        return Consult.objects.create(
            date=date,
            time=time,
        )