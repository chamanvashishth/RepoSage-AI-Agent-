from pydantic import BaseModel, Field, HttpUrl


class AnalyzeRequest(BaseModel):
    repository_url: HttpUrl


class FixRequest(BaseModel):
    repository_url: HttpUrl
    issue_id: str = Field(min_length=3)


class ValidateRequest(BaseModel):
    repository_path: str = Field(min_length=1)


class PullRequestRequest(BaseModel):
    repository_url: HttpUrl
    title: str = Field(min_length=5)
    body: str = Field(min_length=10)
    branch_name: str = Field(min_length=3)
