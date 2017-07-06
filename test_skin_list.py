from services import auth, main


def test_skin_list():
    auth.registration()
    auth.confirm()
    auth.establish()
    skin_list = main.screen()
    print skin_list
    print len(skin_list)
    return skin_list

