import requests
import json
import yaml
from mico.settings import salt_api_url,salt_user,salt_password

class SaltApi(object):
    def __init__(self):
        self.__loginUrl = salt_api_url + '/login'
        self.__url = salt_api_url
        self.__username = salt_user
        self.__password = salt_password
        self.__token_id = self.salt_login()


    def salt_login(self):
        params = {'eauth': 'pam',
                  'username': self.__username,
                  'password': self.__password
                  }
        headers = {'Accept': 'application/json'}
        obj = requests.post(self.__loginUrl,headers=headers,data=params,verify=False).content
        data = json.loads(obj)
        token = data['return'][0]['token']
        return token

    def salt_cmd(self,data):
        self.data = data
        headers = {'Accept': ' application/x-yaml',
                   'X-Auth-Token': ' %s' % self.__token_id
                   }
        obj = requests.post(self.__url,headers=headers,data=self.data,verify=False).content
        try:
            print yaml.load(obj)
            return yaml.load(obj)
        except Exception, e:
	    print obj
            print e
            return 0
