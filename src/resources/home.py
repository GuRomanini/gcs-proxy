import os
import falcon

from constants import COMMIT


class Home:
    def on_get(self, req, resp):
        resp.status = falcon.code_to_http_status(200)

        resp.media = {"VERSION": COMMIT, "PID": str(os.getpid())}
