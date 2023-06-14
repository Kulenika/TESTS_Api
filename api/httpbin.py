from api.client import Client


class HttpBinApi(Client):
    HTML = '/html'
    BASE_URL = 'http://httpbin.org'
    ROBOTS = '/robots.txt'
    IP = '/ip'
    TIME = '/delay'

    def list_html(self):
        '''
        :method:  get
        :routs:   /html
        :status:  200
        '''
        url = self.BASE_URL + self.HTML
        return self.get(url)

    def robots(self):
        '''
        :method:  get
        :routs:   /robots.txt
        :status:  200
        '''
        url = self.BASE_URL + self.ROBOTS
        return self.get(url)

    def ip(self):
        '''
        :method:  get
        :routs:   /ip
        :status:  200
        '''
        url = self.BASE_URL + self.IP
        return self.get(url)

    def time_out(self, delay=1):  #delay - время, за которое мы тестируем.
        '''

        :method: get
        :routs: /delay/{delay}
        status: 200
        '''
        url = self.BASE_URL + self.TIME + f'/3'
        try:
            return self.get(url, timeout=delay)
        except Exception as ex:
            return False, ex

http_bin_api = HttpBinApi()