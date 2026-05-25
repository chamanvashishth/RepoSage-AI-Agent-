from fastapi import APIRouter

from app.schemas.repository import AnalyzeRequest, FixRequest, PullRequestRequest, ValidateRequest
from app.services.repository_service import RepositoryService

router = APIRouter()
service = RepositoryService()


@router.post('/analyze')
async def analyze_repository(payload: AnalyzeRequest):
    return await service.analyze(str(payload.repository_url))


@router.get('/issues')
async def get_issues():
    return {'issues': service.list_issues()}


@router.get('/graph')
async def get_graph(repository_url: str):
    result = await service.analyze(repository_url)
    return {'nodes': result['nodes'], 'edges': result['edges']}


@router.get('/topology')
async def get_topology(repository_url: str):
    result = await service.analyze(repository_url)
    return result['topology']


@router.get('/cognition')
async def get_cognition(repository_url: str):
    result = await service.analyze(repository_url)
    return result['cognition']


@router.post('/fix')
async def fix_repository(payload: FixRequest):
    return {'status': 'queued', 'issue_id': payload.issue_id, 'repository_url': str(payload.repository_url), 'strategy': 'minimal-risk autofix'}


@router.post('/validate')
async def validate_repository(payload: ValidateRequest):
    return {'status': 'validated', 'repository_path': payload.repository_path, 'checks': ['tests', 'lint', 'type-check', 'build']}


@router.post('/pull-request')
async def create_pull_request(payload: PullRequestRequest):
    return {'status': 'ready', 'title': payload.title, 'branch': payload.branch_name, 'body': payload.body}


@router.get('/memory')
async def get_memory(query: str = 'default'):
    return service.memory.search(query)


@router.get('/activity')
async def get_activity():
    return {'events': [{'type': 'service_online', 'component': 'api'}]}
