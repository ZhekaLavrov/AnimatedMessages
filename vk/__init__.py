import random
import time

import requests


class Utils:
    @staticmethod
    def get_random_id():
        return random.randint(-2_147_483_648, 2_147_483_647)


class VK(object):
    def __init__(self, token, version="5.161"):
        self.token = token
        self.version = version

    def _method(self, method, **params):
        params.update(
            {
                "access_token": self.token,
                "v": self.version
            }
        )
        params = "&".join([f"{key}={value}" for key, value in params.items()])

        response = requests.get(f"https://api.vk.com/method/{method}?{params}")
        return response.json()

    def send_message(self, peer_id, text):
        """
        Отправляет сообщение содержащее только текст.
        :return: id сообщения
        """
        _message = self._method("messages.send",
                                peer_id=peer_id,
                                random_id=Utils.get_random_id(),
                                message=text).get("response")
        return _message

    def edit_message(self, peer_id, message_id, text):
        """
        Изменяет текст сообщения.
        :return: 1 - успешно.
        """
        response = self._method("messages.edit",
                                peer_id=peer_id,
                                message_id=message_id,
                                message=text).get("response")
        return response


if __name__ == '__main__':
    import config

    token = config.group_token
    peer_id = config.peer_id
    vk = VK(token)
    message = vk.send_message(peer_id, "❤💚💛")
    print(message)
    # time.sleep(0.5)
    # status = vk.edit_message(peer_id, message, "Hello World!!")
    # print(status)
    # time.sleep(0.5)
    # status = vk.edit_message(peer_id, message, "Hello World!!!")
    # print(status)
    # time.sleep(0.5)
