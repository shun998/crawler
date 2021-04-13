# python执行一段更加复杂的lua脚本

import requests
from urllib.parse import quote

lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://www.baidu.com")
        return {
            html = treat.as_string(response.body),
            url = response.url,
            status = response.status
        }    
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)