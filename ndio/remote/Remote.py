import requests

class Remote(object):
    def __init__(self, hostname, protocol):
        """
        Arguments:
            `hostname`:     Hostname (e.g. google.com)
            `protocol`:     HTTP protocol (e.g. https)
        """
        self.protocol = protocol
        self.hostname = hostname

    def url(self):
        """
        Get the base URL of the Remote.

        Arguments:
            None
        Returns:
            `str` base URL
        """
        return self.protocol + "://" + self.hostname + "/ocp/ca/"


    def ping(self, endpoint=''):
        """
        Ping the server to make sure that you can access the base URL.

        Arguments:
            None
        Returns:
            `boolean` Successful access of server (or status code)
        """
        r = requests.get(self.url() + "/" + endpoint)
        return r.status_code
