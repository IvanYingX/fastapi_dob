import fastapi

router = fastapi.APIRouter()


@router.get('/')
def index():
    return 'Welcome to the AI Core DOB Service'


@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/ai_core.ico')
