from cool.views import CoolAPIException, CoolBFFAPIView, ErrorCode, ViewSite
import os
import logging
logger = logging.getLogger('log')
site = ViewSite(name='App', app_name='App')

def command(command_list):
    command = ''
    for s in command_list:
        command = command + s + " && "
    return command[0:-4]


COMMANDS = {
    "TEAM_JT/ChileCat":{
        "refs/heads/master":[
            'cd /project/ChileCat/django',
            'git fetch --all',
            'git reset --hard origin/master',
            'git pull',
            'systemctl stop ChileCat.service',
            'systemctl start ChileCat.service',
            'systemctl status ChileCat.service'
        ],
        "refs/heads/Develop":[
            'cd /project/ChileCatTest/django',
            'git fetch --all',
            'git reset --hard origin/Develop',
            'git pull',
            'systemctl stop ChileCatTest.service',
            'systemctl start ChileCatTest.service',
            'systemctl status ChileCatTest.service'
        ],
    },
    "TEAM_JT/smart-cloud-uni-app":{
        "refs/heads/master":[
            'cd /project/ChileCat/Uni',
            'git fetch --all',
            'git reset --hard origin/master',
            'git pull'
        ],
        "refs/heads/Dev":[
            'cd /project/ChileCatTest/Uni',
            'git fetch --all',
            'git reset --hard origin/Dev',
            'git pull'
        ],
    },
    "TEAM_JT/ChileCat_Admin_Web":{
        "refs/heads/master":[
            'cd /project/ChileCat/Admin',
            'git fetch --all',
            'git reset --hard origin/master',
            'git pull'
        ],
        "refs/heads/Develop":[
            'cd /project/ChileCatTest/Admin',
            'git fetch --all',
            'git reset --hard origin/Develop',
            'git pull'
        ],
    },
    "TEAM_JT/chile-cat-doc":{
        "refs/heads/master":[
            'cd /project/ChileCat/doc',
            'git fetch --all',
            'git reset --hard origin/master',
            'git pull'
        ]
    }
}

@site
class Hook(CoolBFFAPIView):
    name = ('自动部署')
   
    def get_context(self, request, *args, **kwargs):
        email = request.data["user"]["email"] == "2810201146@qq.com"
        if not email:
            logger.error('身份错误')
            return

        ref = request.data['ref'] # refs/heads/master
        full_name = request.data["repository"]["full_name"] # ChileCat-Django
        
        logger.info('执行更新：'+ref+"："+full_name)
        
        sh = COMMANDS[full_name][ref]
        command_str = command(sh)
        message = os.popen(command_str).readlines()
        logger.info(self.name+'执行结果：')
        for msg in message:
            logger.info(msg)


urls = site.urls
urlpatterns = site.urlpatterns
