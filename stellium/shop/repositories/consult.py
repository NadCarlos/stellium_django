from typing import List, Optional

from shop.models import Consult


class ConsultRepository:

    def get_all(self) -> List[Consult]:
        return Consult.objects.all()