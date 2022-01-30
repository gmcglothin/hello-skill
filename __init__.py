from mycroft import MycroftSkill, intent_file_handler


class Hello(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hello.intent')
    def handle_hello(self, message):
        self.speak_dialog('hello')


def create_skill():
    return Hello()

