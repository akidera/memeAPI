import pytest
from endpoints.auth_endpoint import GetAuthToken
from endpoints.check_token_endpoint import CheckAuthToken
from endpoints.create_meme_endpoint import CreateMeme
from endpoints.delete_meme_endpoint import DeleteMeme
from endpoints.get_meme_list_endpoint import GetMemeList
from endpoints.get_meme_by_id_endpoint import GetMemeById
from endpoints.update_meme_endpoint import UpdateMeme
from endpoints.BaseEndpoint import BaseEdpoint


@pytest.fixture()
def auth_token():

    def get_new_token():
        return GetAuthToken().get_token()

    def is_token_alive(token):
        return CheckAuthToken().check_token(token)

    while True:
        token = get_new_token()
        if is_token_alive(token):
            break
        yield token

    yield token


@pytest.fixture()
def get_auth_token():
    return GetAuthToken()


@pytest.fixture()
def check_auth_token():
    return CheckAuthToken()


@pytest.fixture()
def create_meme():
    return CreateMeme()


@pytest.fixture()
def update_meme():
    return UpdateMeme()


@pytest.fixture()
def get_meme_by_id():
    return GetMemeById()


@pytest.fixture()
def get_meme_list():
    return GetMemeList()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def del_meme():
    meme_ids = []
    yield meme_ids
    token = GetAuthToken().get_token()

    for id in meme_ids:
        DeleteMeme().delete_meme(token=token, meme_id=id)
        print(f'\nmeme with {id} was deleted')


@pytest.fixture()
def create_del_meme():
    token = GetAuthToken().get_token()
    data = CreateMeme().create_meme(token=token)
    yield data
    DeleteMeme().delete_meme(token=token, meme_id=data.id)
    print(f'\nmeme with {data.id} was deleted')
