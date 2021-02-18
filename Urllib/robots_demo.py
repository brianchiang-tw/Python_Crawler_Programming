from urllib.robotparser import RobotFileParser
from urllib import request

robot = RobotFileParser()

url = 'https://www.jianshu.com/robots.txt'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Host':'www.jianshu.com',
}

req = request.Request(url=url, headers = headers )

robot_file_content = request.urlopen(req).read().decode('utf-8').split('\n')
robot.parse( robot_file_content )

# expected output
# True
print( robot.can_fetch('*', 'https://www.jd/com') )

# expected output
# True
print( robot.can_fetch('*', 'https://www.jainshu.com/p/92f6ac2c350f') ) 

# expected output
# False
print( robot.can_fetch('*', 'https://www.jianshu.com/search?q=Python&page=1&type=note') )

