from base64 import *

def dec(msg):
    msg = msg.replace("$eNcRYpt3D$"," ")
    msg = msg.split(" ")
    txt = []
    for i in (msg):
        try:
            txt.append(chr(int(i)))
        except:
            continue

    txt = ''.join(txt) + "="
    txt = b64decode(txt)
    txt = txt[::-1]
    return txt

if __name__ == '__main__':

    msg1 = "90$eNcRYpt3D$50$eNcRYpt3D$53$eNcRYpt3D$104$eNcRYpt3D$99$eNcRYpt3D$50$eNcRYpt3D$70$eNcRYpt3D$119$eNcRYpt3D$99$eNcRYpt3D$109$eNcRYpt3D$86$eNcRYpt3D$48$eNcRYpt3D$73$eNcRYpt3D$71$eNcRYpt3D$104$eNcRYpt3D$104$eNcRYpt3D$90"
    msg2 = "73$eNcRYpt3D$72$eNcRYpt3D$49$eNcRYpt3D$108$eNcRYpt3D$98$eNcRYpt3D$88$eNcRYpt3D$77$eNcRYpt3D$120$eNcRYpt3D$99$eNcRYpt3D$106$eNcRYpt3D$66$eNcRYpt3D$121$eNcRYpt3D$99$eNcRYpt3D$106$eNcRYpt3D$78$eNcRYpt3D$85$eNcRYpt3D$88$eNcRYpt3D$49$eNcRYpt3D$112$eNcRYpt3D$104$eNcRYpt3D$100$eNcRYpt3D$71$eNcRYpt3D$52$eNcRYpt3D$48$eNcRYpt3D$99$eNcRYpt3D$106$eNcRYpt3D$78$eNcRYpt3D$105$eNcRYpt3D$101$eNcRYpt3D$48$eNcRYpt3D$90$eNcRYpt3D$85$eNcRYpt3D$81$eNcRYpt3D$50$eNcRYpt3D$70$eNcRYpt3D$116$eNcRYpt3D$89$eNcRYpt3D$85$eNcRYpt3D$99$eNcRYpt3D$103$eNcRYpt3D$73$eNcRYpt3D$71$eNcRYpt3D$104$eNcRYpt3D$104$eNcRYpt3D$98$eNcRYpt3D$71$eNcRYpt3D$70$eNcRYpt3D$107$eNcRYpt3D$89$eNcRYpt3D$83$eNcRYpt3D$66$eNcRYpt3D$112$eNcRYpt3D$99$eNcRYpt3D$50$eNcRYpt3D$70$eNcRYpt3D$50$eNcRYpt3D$97$eNcRYpt3D$88$eNcRYpt3D$82$eNcRYpt3D$114$eNcRYpt3D$89$eNcRYpt3D$83$eNcRYpt3D$66$eNcRYpt3D$108$eNcRYpt3D$90$eNcRYpt3D$71$eNcRYpt3D$57$eNcRYpt3D$114$eNcRYpt3D$73$eNcRYpt3D$67$eNcRYpt3D$120$eNcRYpt3D$116$eNcRYpt3D$89$eNcRYpt3D$87$eNcRYpt3D$120$eNcRYpt3D$104$eNcRYpt3D$98$eNcRYpt3D$83$eNcRYpt3D$66$eNcRYpt3D$114$eNcRYpt3D$98$eNcRYpt3D$51$eNcRYpt3D$78$eNcRYpt3D$108$eNcRYpt3D$89$eNcRYpt3D$105$eNcRYpt3D$66$eNcRYpt3D$117$eNcRYpt3D$89$eNcRYpt3D$87$eNcRYpt3D$116$eNcRYpt3D$114$eNcRYpt3D$89$eNcRYpt3D$87$eNcRYpt3D$82$eNcRYpt3D$108$eNcRYpt3D$98$eNcRYpt3D$71$eNcRYpt3D$108$eNcRYpt3D$107$eNcRYpt3D$73$eNcRYpt3D$72$eNcRYpt3D$66$eNcRYpt3D$104$eNcRYpt3D$97$eNcRYpt3D$88$eNcRYpt3D$77$eNcRYpt3D$103$eNcRYpt3D$98$eNcRYpt3D$87$eNcRYpt3D$57$eNcRYpt3D$67$eNcRYpt3D$"
    msg3 = "84$eNcRYpt3D$86$eNcRYpt3D$66$eNcRYpt3D$84$eNcRYpt3D$77$eNcRYpt3D$122$eNcRYpt3D$73$eNcRYpt3D$120$eNcRYpt3D$101$eNcRYpt3D$68$eNcRYpt3D$65$eNcRYpt3D$103$eNcRYpt3D$79$eNcRYpt3D$109$eNcRYpt3D$49$eNcRYpt3D$112$eNcRYpt3D$99$eNcRYpt3D$109$eNcRYpt3D$108$eNcRYpt3D$110$eNcRYpt3D$98$eNcRYpt3D$109$eNcRYpt3D$86$eNcRYpt3D$81$eNcRYpt3D$"

#    print dec(msg1)
    print dec(msg2)
#    print dec(msg3)
