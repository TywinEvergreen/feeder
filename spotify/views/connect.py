from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from spotipy import oauth2

from feeder import settings


class ConnectSpotifyAccountApiView(APIView):
    """
    Connect user's spotify account to the service
    GET to retrieve the user authorization url
    POST to process the authorization code
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.oauth_client = oauth2.SpotifyOAuth(
            settings.SPOTIFY_CLIENT_ID,
            settings.SPOTIFY_CLIENT_SECRET,
            settings.SPOTIFY_REDIRECT_URI,
            scope="user-follow-read",
        )

    def get(self, request, *args, **kwargs) -> Response(dict):
        return Response({"authorize_url": self.oauth_client.get_authorize_url()})

    def post(self, request, *args, **kwargs) -> Response(str):
        code = request.query_params.get("code")
        if not code:
            return Response("no_code_error", status=status.HTTP_400_BAD_REQUEST)

        # TODO: Token obtaining is done, need to finish the main logic
        self.oauth_client.get_access_token(code)
        return Response()
