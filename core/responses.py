from dataclasses import asdict, dataclass

@dataclass
class ApiErrorResponse:

    timestamp: str
    status: int
    error: str
    message: str
    path: str

    def to_dict(self):
        return asdict(self)