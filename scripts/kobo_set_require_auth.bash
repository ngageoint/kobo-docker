#!/bin/bash
set -e

cat << EOF > set_require_auth.py
import re
filename = './onadata/apps/main/models/user_profile.py'
content = open(filename).read()
content = re.sub('(require_auth = models.BooleanField\(\s+)default=False','\g<1>default=True',content,re.M|re.DOTALL)
fp = open(filename,'w')
fp.write(content)
fp.close()
EOF
python set_require_auth.py
/bin/rm set_require_auth.py

sed "s/'require_auth', models.BooleanField(default=False/'require_auth', models.BooleanField(default=True/g" ./onadata/apps/main/migrations/0001_initial.py

