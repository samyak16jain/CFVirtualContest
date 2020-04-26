import requests, json, os, hashlib, time, sys
from auth import key , secret, handle
from random import randint

os.system("clear")
curr_time = int(round(time.time()))
url = "http://codeforces.com/api/"
rand = randint(100000,999999)

def jprint(obj):
    st = json.dumps(obj,indent=4,sort_keys=True)
    print(st)

def get_hash(meth):
    hash = hashlib.sha512(str.encode(f"{rand}/{meth}?apiKey={key}&time={curr_time}#{secret}"))
    return hash.hexdigest()

def get_status(id):
    req = requests.get(f"https://codeforces.com/api/contest.status?contestId={id}&handle={handle}")
    if len(req.json()['result']) == 0:
        return True
    else:
        return False

def get_id(type):
    apiSig=get_hash("contest.list")

    req = requests.get("http://codeforces.com/api/{}?apiKey={}&time={}&apiSig={}{}".format("contest.list",key,curr_time,rand,apiSig))

    id = -1
    for contest in req.json()['result']:
        b = False
        if contest['name'].find(f'{type}') !=-1 and contest['durationSeconds']==7200 and contest['phase']=='FINISHED' :
            b = get_status(contest['id'])
            if b:
                id = contest['id']
                break
            
    return str(id)

id = get_id("Div. "+sys.argv[1])
f = open("contestID.txt",'w')
f.write(id)
f.close()
