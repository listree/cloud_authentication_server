from django.http import HttpResponse
import uuid, sqlite3

#use this endpoint: /auth/chkkey to check if key/secret matches
def chkkey(request):

    if 'key' in request.GET and 'secret' in request.GET :
        key = request.GET['key']
        secret = request.GET['secret']
        conn = sqlite3.connect("auth.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM key_secret WHERE key = '%s' and secret = '%s'" % (key, secret))
        row = cur.fetchall()
        if(len(row) > 0) :
            return HttpResponse("OK")
        else :
            return HttpResponse("NO")
        conn.close()
    else:
        return HttpResponse("KO")

#use this endpoint: /auth/genkey to generate new pair of key secret
def genkey(request):
    key = uuid.uuid1().hex
    secret = uuid.uuid1().hex
    conn = sqlite3.connect("auth.db")
    cur = conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS key_secret (key text NOT NULL, secret text NOT NULL)")
    cur.execute("INSERT INTO key_secret VALUES ('%s','%s')" % (key, secret))
    conn.commit()
    conn.close()
    return HttpResponse('"' + key + '":"' + secret + '"')