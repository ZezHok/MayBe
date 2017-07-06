from services import auth, main


def test_skin_list():
    phone = ["+73330001100", "73330001117"]
    skin_list = []
    for i in range(len(phone)):
        num = phone[i]
        auth.registration(phone[i])
        auth.confirm(phone[i])
        auth.establish(phone[i])
        a = main.screen(phone[i])
        for n in range(len(a)):
            skin_list.append(a[n])
    return skin_list

def test():
    print test_skin_list()[0][0]
    print ("!!!!!")
    print test_skin_list()[1][0]


