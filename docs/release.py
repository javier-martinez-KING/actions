#!/usr/bin/python3
from pathlib import Path

#import katserverapi


pipfile = '''
[[source]]
verify_ssl = false
name = "artifactory-edge"
url = "https://artifactory-edge.ess.midasplayer.com/artifactory/api/pypi/pypi-all/simple/"

[dev-packages]
katserverapi = "*"

[requires]
python_version = "3.9"
'''


'''
GUID_dev = "80845309-51c6-448a-a29f-847617a6c775"
GUID = ""

ROOT = Path(__file__).parent
module_version = (ROOT / "VERSION").read_text().strip()
mversion = '0.0.0'

def update_version():
    pass


update_version(module_version)

# Add KAT-META
interface = katserverapi.get_production_interface()
interface.register_new_package_version(GUID, module_version,
                                       url=f"https://github.int.midasplayer.com/TechArt/witcher/releases/download/v{module_version}/witcher-{module_version}.zip",
                                       application_version=mversion)
'''

'''
import requests
import json
guid = 'df228025-a709-429c-80d5-6c3e291fe7e8'

data = {
  "url": "",
  "url_win": "https://download.sublimetext.com/sublime_text_build_4126_x64-0.0.1.zip",
  "url_osx": "",
  "setup": "",
  "setup_win": "exec ",
  "setup_osx": "exec ",
  "start": "",
  "start_win": "exec ",
  "start_osx": "exec ",
  "application_version": "0.0.1",
  "requires_app_restart": True
}
url = 'https://king-kat-dev.appspot.com/api/v1/'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url+'package/'+guid+'/version/0.0.1', data=json.dumps(data), headers=headers)

r.status_code
print(r.json())
'''


'''
import requests
import json


data = {
  "name": "mayafiction2",
  "target": "maya",
  "description": "This is the beta release for next raike exporter for maya",
  "documentation": "wip",
  "icon": "wip",
  "visible": True
}
url = 'https://king-kat-dev.appspot.com/api/v1/'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


r = requests.post(url+'package/', data=json.dumps(data), headers=headers)
print(r.status_code)
print(r)
print(r.json())



r = requests.get(url+'package/targets', headers=headers)
print(r.status_code)
print(r.json())
'''

# Add KAT-META
#interface = katserverapi.get_production_interface()
#interface.register_new_package('mayafiction', 'maya')



  
def do_release(*ags, **kws):
    from js import Blob, document
    from js import window
  
    with open('/test.txt', 'rt') as fh:
        txt = fh.read()
        
    blob = Blob.new([txt], {type : 'application/text'})
    url = window.URL.createObjectURL(blob) 
    window.location.assign(url)
