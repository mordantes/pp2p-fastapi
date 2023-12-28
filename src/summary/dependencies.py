from src.summary.service import SummaryService
from src.database import session_maker


def get_service():
    return SummaryService(session_maker)
