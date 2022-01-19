from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def foo():
    return {'qwert': 'fgbhj'}
