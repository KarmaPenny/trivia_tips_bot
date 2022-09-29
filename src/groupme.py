from requests import Session


class GroupMe:
    """Client for interacting with GroupMe API. https://dev.groupme.com/docs/v3"""

    def __init__(self, access_token: str):
        """instantiates a new GroupMe client

        Args:
          access_token: the access token to authenticate with
        """

        # create http session with GroupMe authentication headers
        self.session = Session()
        self.session.headers = {
            "X-Access-Token": access_token,
        }

    def post(self, bot_id: str, message: str):
        """posts a message to a GroupMe group

        Args:
          bot_id: the id of the bot to post as
          message: the message to post
        """

        # post the message to the group
        r = self.session.post(
            f"https://api.groupme.com/v3/bots/post",
            json={
                "bot_id": bot_id,
                "text": message,
            },
        )
        r.raise_for_status()
