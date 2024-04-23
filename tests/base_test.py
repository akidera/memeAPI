from endpoints.auth_endpoint import GetAuthToken
from endpoints.check_token_endpoint import CheckAuthToken
from endpoints.create_meme_endpoint import CreateMeme
from endpoints.update_meme_endpoint import UpdateMeme
from endpoints.get_meme_by_id_endpoint import GetMemeById
from endpoints.get_meme_list_endpoint import GetMemeList
from endpoints.delete_meme_endpoint import DeleteMeme


class BaseTest:
    create_endpnt: CreateMeme = CreateMeme()
    update_endpnt: UpdateMeme = UpdateMeme()
    get_by_id_endpnt: GetMemeById = GetMemeById()
    get_list_endpoint: GetMemeList = GetMemeList()
    get_auth_endpnt: GetAuthToken = GetAuthToken()
    check_auth_endpnt = CheckAuthToken = CheckAuthToken()
    delete_enpnt: DeleteMeme = DeleteMeme()
