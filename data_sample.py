from dataclasses import dataclass
from datetime import datetime

from authorities import Authorities


@dataclass
class Sample:
    timestamp: datetime
    preferences: [Authorities]
    final: Authorities
