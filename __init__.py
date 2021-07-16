from mycroft import MycroftSkill, intent_file_handler


class Mpc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mpc.intent')
    def handle_mpc(self, message):
        self.speak_dialog('mpc')


def create_skill():
    return Mpc()

