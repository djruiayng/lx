# -*- coding: utf-8 -*-
from Linephu.linepy import *
#from thrift import*
from datetime import datetime
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
import timeit

botStart = time.time()
cl = LINE("djry0416@gmail.com","djry9420")
k1 = LINE("nolga3398@gmail.com","djry9420")
k2 = LINE("og773030@gmail.com","djry9420")
k3 = LINE("ogorinivic@gmail.com","djry9420")
k4 = LINE("zgoryunova59@gmail.com","djry9420")
print ("[ 登錄系統 ]成功(  -᷄ω-᷅ )")
clMID = cl.profile.mid
k1MID = k1.profile.mid
k2MID = k2.profile.mid
k3MID = k3.profile.mid
k4MID = k4.profile.mid

Bots = [clMID,k1MID,k2MID,k3MID,k4MID]
god = ['u7dee0949b799e28a38085c0660a99ab2']
oepoll = OEPoll(cl)

banOpen = codecs.open("ban.json","r","utf-8")
groupOpen = codecs.open("group.json","r","utf-8")
proOpen = codecs.open("pro.json","r","utf-8")
ban = json.load(banOpen)
gp = json.load(groupOpen)
pro = json.load(proOpen)
#==============================================================================#
def restartBot():
    print ("[ 重新啟動系統 ] 成功(  -᷄ω-᷅ )")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def botJoin(to):
    G = cl.getGroup(to)
    G.preventedJoinByTicket = False
    cl.updateGroup(G)
    Ticket = cl.reissueGroupTicket(op.param1)
    k1.acceptGroupInvitationByTicket(to,Ticket)
    k2.acceptGroupInvitationByTicket(to,Ticket)
    k3.acceptGroupInvitationByTicket(to,Ticket)
    k4.acceptGroupInvitationByTicket(to,Ticket)
    G.preventedJoinByTicket = True
    cl.updateGroup(G)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invaliod mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
            textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def backupData():
    try:
        backup = ban
        f = codecs.open('ban.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = gp
        f = codecs.open('group.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = pro
        f = codecs.open('pro.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)		
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ 後台錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """🔥 〘弑神 戰爭〙 🔥  
🔥   Gc-剩餘票數
🔥   速度-速度
🔥   Test-速度
🔥   Bj-機器進入
🔥   By-機器退出
🔥   Godd @-新增群管
🔥   Godl @-刪除群管
🔥   GM-查看本群管理者
🔥   Bl-黑單
🔥   Adminlist-權限者清單
🔥   標記-全員標記
╚〘作者:🔥  戰爭機器 🔥  〙"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""🔥 〘弑神 戰爭〙 🔥  
🔥   Gadd @-新增群管
🔥   Gdel @-刪除群管
🔥   GM-查看本群管理者
🔥   重啟-重新啟動
🔥   踢 @-多標踢人
🔥🔥🔥 保護開啟/關閉 🔥🔥🔥
🔥   全部保護開啟-全部保護開啟
🔥   全部保護關閉-全部保護關閉
🔥🔥🔥 票券/權限指令 🔥🔥🔥
🔥   Gc mid-查看票數
🔥   Add-新增權限
🔥   Del-取消權限
🔥   A mid-給票
🔥   票券 -查詢票券
🔥   lv1-3_add-加入權限
🔥   admin- 查詢權限使用者
🔥   clear lvx-清空所有權限者
🔥  read on/off -查看已讀者
🔥🔥🔥 黑單指令 🔥🔥🔥
🔥 Ban:mid-使用Mid黑單
🔥 /ban-友資黑單
🔥 Ban @-標註黑單
🔥 Unban:mid-使用mid解黑
🔥 Unban-友資解黑
🔥 /unban @-標注黑單
🔥 速度-速度
🔥 .hi-報數
🔥 Adminlist-普通權限者
🔥 ownerlist-最高權限者
🔥 Admin-lv1-3權限者
🔥 Clear ban-清除黑單
🔥 Kg-全群掃黑
🔥 Kill ban-當前群組掃黑
╚〘作者:🔥  戰爭機器 🔥〙"""
    return helpMessageTag
def helpn():
    helpN = """ 🔥 〘弑神 戰爭〙 🔥
🔥 Gc-查詢自己剩餘票數
🔥 速度-速度
🔥 GM-查看本群管理者
╚〘作者:🔥  戰爭機器 🔥 〙"""
    return helpN

wait = {
    "ban" : False,
    "unban" : False,
    "add" : False,
    "rapidFire":{},		
    "del" : False
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
msg_dict = {}
bl = [""]

if clMID not in ban["owners"]:
    ban["owners"].append(clMID)
if k1MID not in ban["owners"]:
    ban["owners"].append(k1MID)
if k2MID not in ban["owners"]:
    ban["owners"].append(k2MID)
if k3MID not in ban["owners"]:
    ban["owners"].append(k3MID)
if k4MID not in ban["owners"]:
    ban["owners"].append(k4MID)
if "u7dee0949b799e28a38085c0660a99ab2" not in ban["owners"]:
    ban["owners"].append("u7dee0949b799e28a38085c0660a99ab2")
def lineBot(op):
    try:	
        if op.type == 11:
            G = cl.getGroup(op.param1)
            if op.param1 in pro["qrprotect"]:
                if op.param2 in ban["owners"] or op.param2 in ban["admin"] :
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    if G.id in gp["s"] and op.param2 in gp["s"][G.id]:
                        pass	
                    else:						
                        bot =[cl,k1,k2,k3,k4]			
                        k123=random.choice(bot)			
                        gs = cl.getGroup(op.param1)
                        k123.sendMessage(op.param1,cl.getContact(op.param2).displayName + "🔥網址保護中...不要動群組網址！🔥")						
                        k123.kickoutFromGroup(op.param1,[op.param2])
                        gs.preventedJoinByTicket = False
                        gs.preventedJoinByTicket = True
                        k123.updateGroup(gs)	
        if op.type == 5:
            cl.findAndAddContactsByMid(op.param1) 
            cl.sendMessage(op.param1, "🔥你好 {} 謝謝你加我為好友，如有需求請向以下友資購買票卷 ".format(str(cl.getContact(op.param1).displayName)))
            cl.sendContact(op.param1,'u4ace3ef40dc897bdcee947d184909199')
        if op.type ==19:
            a = 0
            if op.param2 in ban["admin"] or op.param2 in ban["owners"]:
                if op.param3 in clMID or op.param3 in k1MID or op.param3 in k2MID or op.param3 in k3MID or op.param3 in k4MID :
                    while (a<3):
                        try:
                            bot = random.choice([cl,k1,k2,k3,k4])
                            G = bot.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            bot.updateGroup(G)
                            Ticket = bot.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            a+=1
                            continue
                        else:
                            break
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
            elif op.param3 in clMID or op.param3 in k1MID or op.param3 in k2MID or op.param3 in k3MID or op.param3 in k4MID:
                while (a<3):
                    try:
                        bot = random.choice([cl,k1,k2,k3,k4])
                        bot.kickoutFromGroup(op.param1,[op.param2])
                        G = bot.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        bot.updateGroup(G)
                        Ticket = bot.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)					
                    except:
                        a+=1
                        continue
                    else:
                        break
                try:
                    ban["blacklist"][op.param2] = True
                    G = bot.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    bot.updateGroup(G)
                except:
                    pass
        if op.type == 19:
            G = cl.getGroup(op.param1)
            if op.param1 in pro["protect"]:
                bot = random.choice([cl,k1,k2,k3,k4])
                G=bot.getGroup(op.param1)
                if op.param2 in ban["owners"] or op.param2 in ban["admin"] :
                    pass
                else:
                    bot.kickoutFromGroup(op.param1,[op.param2])
                    ban["blacklist"][op.param2] = True
            if op.param3 in ban["owners"]:
                bot = random.choice([cl,k1,k2,k3,k4])
                bot.findAndAddContactsByMid(op.param3)
                bot.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 13:
            G = cl.getGroup(op.param1)
            if op.param1 in pro["invprotect"]:
                if op.param2 in ban["owners"] or op.param2 in ban["admin"] :
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    if G.id in gp["s"] and op.param2 in gp["s"][G.id]:
                        pass	
                    else:	
                        bot = random.choice([cl,k1,k2,k3,k4])					
                        bot.cancelGroupInvitation(op.param1,[op.param3])
                        bot.kickoutFromGroup(op.param1,[op.param2])
                        ban["blacklist"][op.param2] = True						
        if op.type == 0:
            return
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if clMID in op.param3:
                if op.param2 in ban["owners"] or op.param2 in god:
                    cl.acceptGroupInvitation(op.param1)
                    botJoin(op.param1)
                    gMembMids = [contact.mid for contact in G.members]
                    G = cl.getGroup(op.param1)
                    pro["invprotect"][G.id] = False						
                    pro["qrprotect"][G.id] = False						
                    pro["protect"][G.id] = False	
                    cl.sendMessage(op.param1, "預設全保護開啟")
                    matched_list = []
                    for tag in ban["blacklist"]:
                        if tag in gMembMids:
                            matched_list.append(str(tag))
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        bot = random.choice([cl,k1,k2,k3,k4])
                        bot.kickoutFromGroup(op.param1,[jj])					
                elif op.param2 in ban["user"]:
                    ban["user"][op.param2] =ban["user"][op.param2] -1
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,"🔥你還擁有{}張票🔥".format(str(ban["user"][op.param2])))
                    botJoin(op.param1)
                    if ban["user"][op.param2] == 0:
                        del ban["user"][op.param2]
                    G = cl.getGroup(op.param1)
                    gp["s"][G.id] =[]
                    gp["s"][G.id].append(op.param2)
                    backupData()
                    gMembMids = [contact.mid for contact in G.members]
                    matched_list = []
                    for tag in ban["blacklist"]:
                        if tag in gMembMids:
                            matched_list.append(str(tag))
                    if matched_list == []:
                        return
                    for jj in matched_list:
                        bot = random.choice([cl,k1,k2,k3,k4])
                        bot.kickoutFromGroup(op.param1,[jj])
                else:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,"🔥你的票不夠🔥")
                    cl.leaveGroup(op.param1)
            if k1MID in op.param3:
            	k1.rejectGroupInvitation(op.param1)
            if k2MID in op.param3:
            	k2.rejectGroupInvitation(op.param1)
            if k3MID in op.param3:
            	k3.rejectGroupInvitation(op.param1)
            if k4MID in op.param3:
            	k4.rejectGroupInvitation(op.param1) 				
            elif op.param2 in ban["admin"] or op.param2 in Bots or op.param2 in ban["owners"]:
                pass
            else:
                bot = random.choice([cl,k1,k2,k3,k4])
                G=bot.getGroup(op.param1)
                matched_list = []
                for tag in ban["blacklist"]:
                    if tag in op.param3:
                        matched_list.append(str(tag))
                if matched_list == []:
                    return
                for mid in matched_list:
                    bot.cancelGroupInvitation(op.param1,[mid])
        if op.type == 17:
            if op.param2 in ban["blacklist"]:
                bot = random.choice([cl,k1,k2,k3,k4])
                bot.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if clMID in op.param3:
                cl.leaveRoom(op.param1)
            if k1MID in op.param3:
                k1.leaveRoom(op.param1)
            if k2MID in op.param3:
                k2.leaveRoom(op.param1)
            if k3MID in op.param3:
                k3.leaveRoom(op.param1)
            if k4MID in op.param3:
                k4.leaveRoom(op.param1)
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if wait["ban"] == True:
                    if msg._from in ban["owners"] or msg._from in ban["admin"]:
                        if msg.contentMetadata["mid"] in ban["blacklist"]:
                            cl.sendMessage(msg.to,"已加入黑單")
                            wait["ban"] = False
                        else:
                            ban["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["ban"] = False
                            tz = pytz.timezone("Asia/Makassar")				
                            timeNow = datetime.now(tz=tz)
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            cl.sendMessage(msg.to,"{}".format(contact.displayName)+"\n[加入黑單 時間:【"+timeNow.strftime('%H:%M:%S')+"】"+"]")								
                elif wait["unban"] == True:
                    if msg._from in ban["owners"] or msg._from in ban["admin"]:
                        if msg.contentMetadata["mid"] not in ban["blacklist"]:
                            cl.sendMessage(msg.to,"已不是黑單")
                            wait["unban"] = False
                        else:
                            del ban["blacklist"][msg.contentMetadata["mid"]]
                            wait["unban"] = False
                            tz = pytz.timezone("Asia/Makassar")				
                            timeNow = datetime.now(tz=tz)
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            contact = cl.getContact(msg.contentMetadata["mid"])							
                            cl.sendMessage(msg.to,"{}".format(contact.displayName)+"\n［解除黑單 時間:【"+timeNow.strftime('%H:%M:%S')+"】"+"]")	
        if (op.type == 25 or op.type == 26) and op.message.contentType == 0:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            elif msg.toType == 2:
                to = receiver
            if text.lower() is None:
                return
            if sender in ban["blacklist"]:
                return
            if msg.to in wait["rapidFire"]:
                if time.time() - wait["rapidFire"][msg.to] < 2:
                    return
#                    cl.kickoutFromGroup(to,[sender])
                else:
                    wait["rapidFire"][msg.to] = time.time()
            else:
                wait["rapidFire"][msg.to] = time.time()				
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in god:
                if text.lower() == '重啟':
                    cl.sendMessage(to, "重新啟動")
                    cl.sendMessage(to, "重新啟動中")
                    cl.sendMessage(to, "稍等一分鐘")
                    restartBot()
                elif "Gft:" in msg.text:
                    bctxt = text.replace("Gft:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,"[群組廣播]\n"+bctxt)						
                elif text.lower() == '票卷':
                    if ban["user"] == []:
                        cl.sendMessage(msg.to,"🔥目前沒票🔥")
                    else:
                         try:
                             mc = "[ 票卷名單 ]"
                             for mi_d in ban["user"]:
                                 mc += "\n[ " +cl.getContact(mi_d).displayName + " ]"
                                 mc += "\n   數量:{}".format(str(ban["user"][mi_d]))
                             cl.sendMessage(msg.to,mc + "\n[ 已查完結果 ]")
                         except:
                             pass					
            if sender in ban["owners"] or sender in god:
                if text.lower() =='by':
                    cl.leaveGroup(msg.to)
                    k1.leaveGroup(msg.to)
                    k2.leaveGroup(msg.to)
                    k3.leaveGroup(msg.to)
                    k4.leaveGroup(msg.to)
                    print ("[機器通知] 離開群組！")
                elif text.lower() == 'bj':
                    G = cl.getGroup(to)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(to)
                    k1.acceptGroupInvitationByTicket(to,Ticket)
                    k2.acceptGroupInvitationByTicket(to,Ticket)
                    k3.acceptGroupInvitationByTicket(to,Ticket)
                    k4.acceptGroupInvitationByTicket(to,Ticket)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)					
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to, "儲存完畢")									
                elif text.lower() == 'cb':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")	
                    if clMID not in ban["owners"]:
                        ban["owners"].append(clMID)															
                elif text.lower().startswith("delad:"):
                    txt = text.replace("Unadmin:","")
                    try:
                        del ban["admin"][txt]
                        cl.sendMessage(msg.to,"已刪除!")
                    except:
                        cl.sendMessage(msg.to,"刪除失敗 !" +txt)
            if sender in sender:
                if text.lower() == 'gc':
                    tz = pytz.timezone("Asia/Makassar")				
                    timeNow = datetime.now(tz=tz)
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")					
                    if sender in ban["user"]:
                        cl.sendMessage(to,"你好【{}】\n".format(cl.getContact(sender).displayName)+"剩下{}票".format(str(ban["user"][sender]))+"\n查詢時間:【"+timeNow.strftime('%H:%M:%S')+"】")
                    else:
                        cl.sendMessage(to,"你好[{}]\n".format(cl.getContact(sender).displayName)+"您的票不夠"+"\n查詢時間:【"+timeNow.strftime('%H:%M:%S')+"】")
                elif text.lower() == '票':
                    tz = pytz.timezone("Asia/Makassar")				
                    timeNow = datetime.now(tz=tz)
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")				
                    ret_ = "╔【你好 {} 以下票券查詢】".format(cl.getContact(sender).displayName)
                    if sender in ban["user"]:ret_ += "\n╠剩下{}票卷".format(str(ban["user"][sender]))
                    else:ret_ += "\n╠若票卷不足，請購買" 
                    if sender in god:ret_ += "\n╠使用者權限:最高"					
                    elif sender in ban["admin"]:ret_ += "\n╠ 使用者權限:權限者"
                    else:ret_ += "\n╠ 使用者權限 : 基本(/menu2)"					
                    ret_ += "\n╚[查詢時間:【"+timeNow.strftime('%H:%M:%S')+"】"+"]"
                    cl.sendMessage(to, str(ret_))					
                elif text.lower() == '速度':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == '標記':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    cl.sendMessage(to, "總共 {} 人".format(str(len(nama))))               
                elif text.lower() =='adminall':
                    mc ="Grade\n"
                    no1 = 0
                    mc +="≡≡≡等級1≡≡≡"					
                    for lv1 in ban["lv1"]:
                        no1 += 1
                        mc += "\n{}✔.".format(str(no1))+cl.getContact(lv1).displayName
                    if ban["lv1"] == {}:
                        mc += "\n沒有權限者"						
                    no2 = 0	
                    mc +="\n≡≡≡等級2≡≡≡"					
                    for lv2 in ban["lv2"]:
                        no2 += 1
                        mc += "\n{}✔.".format(str(no2))+cl.getContact(lv2).displayName
                    if ban["lv2"] == {}:
                        mc += "\n沒有權限者"							
                    no3 = 0	
                    mc +="\n≡≡≡等級3≡≡≡"					
                    for lv3 in ban["lv3"]:
                        no3 += 1
                        mc += "\n{}✔.".format(str(no3))+cl.getContact(lv3).displayName
                    if ban["lv3"] == {}:
                        mc += "\n沒有權限者"																
                    cl.sendMessage(to,mc )						
                elif text.lower() == 'test':
                    start = time.time()
                    cl.sendMessage(to, "計算中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == '標記':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                    cl.sendMessage(to, "總共 {} 人".format(str(len(nama))))
                elif text.lower().startswith("踢 "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in ban["owners"]:
                            pass
                        else:
                            try:
                                kicker=random.choice([k1,k2,k3,k4])
                                kicker.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif text.lower() == 'groupgm':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gm':
                    G = cl.getGroup(to)
                    if G.id not in gp["s"] or gp["s"][G.id]==[]:
                        cl.sendMessage(to,"無群管!")
                    else:
                        mc = "╔══[ Group Manager ]"
                        for mi_d in gp["s"][G.id]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔══[ 設定 ]"

                        if msg.toType==2:
                            G = cl.getGroup(msg.to)
                            if G.id in pro["protect"] : ret_+="\n╠ 踢人保護 ✅"
                            else: ret_ += "\n╠ 踢人保護 ❌"
                            if G.id in pro["qrprotect"] : ret_+="\n╠ 網址保護 ✅"
                            else: ret_ += "\n╠ 網址保護 ❌"
                            if G.id in pro["invprotect"] : ret_+="\n╠ 邀請保護 ✅"
                            else: ret_ += "\n╠ 邀請保護 ❌"
                            if ban["reread"] == True: ret_ += "\n╠ 查詢收回開啟 ✅"
                            else: ret_ += "\n╠ 查詢收回關閉 ❌"							
                        ret_ += "\n╚══[ 設定 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))						
                elif text.lower() == '功能':
                    if sender in ban["admin"]:
                        helpMessage = helpmessage()
                        cl.sendMessage(to, str(helpMessage))
                    elif sender in ban["owners"]:
                        helpMessageTag = helpmessagetag()
                        cl.sendMessage(to, str(helpMessageTag))
                    else:
                        helpN = helpn()
                        cl.sendMessage(to, str(helpN))
            if sender in ban["admin"] or sender in ban["owners"]:	
                if text.lower().startswith('lv1_add '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["lv1"][target] = True
                            cl.sendMessage(msg.to,"已加入等級1!")
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                elif text.lower().startswith('lv1_del '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["lv1"][target]
                            cl.sendMessage(msg.to,"刪除權限成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                if text.lower().startswith('lv2_add '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["lv2"][target] = True
                            cl.sendMessage(msg.to,"已加入等級2!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith('lv2_del '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["lv2"][target]
                            cl.sendMessage(msg.to,"刪除權限成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                if text.lower().startswith('lv3_add '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["lv3"][target] = True
                            cl.sendMessage(msg.to,"已加入等級3!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith('lv3_del '):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["lv3"][target]
                            cl.sendMessage(msg.to,"刪除權限成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                if text.lower() == 'clear lvx':
                    for mi_d in ban["lv1"]:
                        ban["lv1"] = {}
                    cl.sendMessage(to, "lv1已清空")							
                    for mi_d in ban["lv2"]:
                        ban["lv2"] = {}
                    cl.sendMessage(to, "lv2已清空")							
                    for mi_d in ban["lv3"]:
                        ban["lv3"] = {}
                    cl.sendMessage(to, "lv3已清空")
                if text.lower() == 'clear lv1':
                    for mi_d in ban["lv1"]:
                        ban["lv1"] = {}
                    cl.sendMessage(to, "lv1已清空")
                if text.lower() == 'clear lv2':
                    for mi_d in ban["lv2"]:
                        ban["lv2"] = {}
                    cl.sendMessage(to, "lv2已清空")				
                if text.lower() == 'clear lv3':
                    for mi_d in ban["lv3"]:
                        ban["lv3"] = {}
                    cl.sendMessage(to, "lv3已清空")
                elif text.lower() == 'clear ban':
                    ban["blacklist"].clear()
                    cl.sendMessage(to, "已清空黑名單")
                    json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)    
                if text.lower() == 'reread on':
                    ban["reread"] = True
                    cl.sendMessage(to,"查詢收回開啟")
                elif text.lower() == 'reread off':
                    ban["reread"] = False
                    cl.sendMessage(to,"查詢收回關閉")
                elif text.lower() == 'qr on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        pro["qrprotect"][G.id] = True
                        cl.sendMessage(to, "網址保護開啟")
                elif text.lower() == 'qr off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del pro["qrprotect"][G.id]
                        except:
                            pass
                        cl.sendMessage(to, "網址保護關閉")
                elif text.lower() == 'kick on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        pro["protect"][G.id] = True
                        cl.sendMessage(to, "踢人保護開啟")
                elif text.lower() == 'kick off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del pro["protect"][G.id]
                        except:
                            pass
                        cl.sendMessage(to, "踢人保護關閉")
                elif text.lower() == 'inv on':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        pro["invprotect"][G.id] = True
                        cl.sendMessage(to, "邀請保護開啟")
                elif text.lower() == 'inv off':
                    if msg.toType ==2 :
                        G = cl.getGroup(msg.to)
                        try:
                            del pro["invprotect"][G.id]
                        except:
                            pass
                        cl.sendMessage(to, "邀請保護關閉")
                elif text.lower() == '全部保護開啟':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        pro["protect"][G.id] = True
                        pro["qrprotect"][G.id] = True
                        pro["invprotect"][G.id] = True
                        cl.sendMessage(to, "踢人保護開啟")
                        cl.sendMessage(to, "邀請保護開啟")
                        cl.sendMessage(to, "網址保護開啟")
                elif text.lower() == '全部保護關閉':
                    if msg.toType ==2:
                        G = cl.getGroup(msg.to)
                        try:
                            del pro["protect"][G.id]
                            cl.sendMessage(to, "踢人保護關閉")
                        except:
                            pass
                        try:
                            del pro["qrprotect"][G.id]
                            cl.sendMessage(to, "網址保護關閉")
                        except:
                            pass
                        try:
                            del pro["invprotect"][G.id]
                            cl.sendMessage(to, "邀請保護關閉")
                            cl.sendMessage(to, "所有保護保護已關閉。")
                        except:
                            pass										
                if text.lower().startswith("gadd "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in gp["s"]:
                        gp["s"][G.id] =[]
                        for x in key["MENTIONEES"]:
                            gp["s"][G.id].append(x["M"])
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        for x in key["MENTIONEES"]:
                            gp["s"][G.id].append(x["M"])
                        cl.sendMessage(to,"OK")	
                if text.lower().startswith("gdel "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    G = cl.getGroup(to)
                    if G.id not in gp["s"]:
                        cl.sendMessage(to, "There is no group manager！")
                    else:
                        for x in key["MENTIONEES"]:
                            try:
                                gp["s"][G.id].remove(x["M"])
                            except:
                                cl.sendMessage(to,"Not in GM.")
                        cl.sendMessage(to,"OK")
                elif text.lower() == 'owners':
                    if ban["owners"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ owners List ]"
                        for mi_d in ban["owners"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")	
                elif text.lower() == 'adminlist':
                    if ban["admin"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ Admin List ]"
                        for mi_d in ban["admin"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")						
                elif text.lower() == 'bl':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"[提示]無黑單成員!")
                    else:
                        mc = "[ Black List ]"
                        for mi_d in ban["blacklist"]:
                            if ban["blacklist"][mi_d] == True:
                                mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)
                            else:
                            	mc += "\n↬ "+cl.getContact(mi_d).displayName+"\n"+str(mi_d)+"[baned]"
                        cl.sendMessage(msg.to,mc + "\n[ Finish ]")
            if sender in ban["owners"] or sender in god:
                if  text.lower() =='兄弟們出來':
                    cl.sendMessage(to,"幹嘛")
                    k1.sendMessage(to,"我來了")
                    k2.sendMessage(to,"別吵我")
                    k3.sendMessage(to," ㄟㄟㄟ我在忙拉")
                    k4.sendMessage(to,"有屁快放!!")
                elif text.lower() == 'rn':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運行 {}".format(str(runtime)))
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'ban':
                    cl.sendMessage(to, "請傳送友資加入黑名單")
                    wait["ban"] = True
                elif text.lower() == 'unban':
                    cl.sendMessage(to, "請傳送友資移除黑名單")
                    wait["unban"] = True
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)				
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif text.lower() == 'me':
                    if msg.toType == 2 or msg.toType == 1:
                        sendMessageWithMention(to, sender)
                        cl.sendContact(to, sender)
                    else:
                        cl.sendContact(to,sender)
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "無"
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ 群名: {}".format(str(group.name))
                    ret_ += "\n╠ 群組 Id : {}".format(group.id)
                    ret_ += "\n╠ 創群人 : {}".format(str(gCreator))
                    ret_ += "\n╠ 目前人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請招待 : {}".format(gPending)
                    ret_ += "\n╠ 群組網址 : {}".format(gQr)
                    ret_ += "\n╠ 網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "網址開啟")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "已經打開了")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "網址關閉")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "已經關閉了")						
                elif text.lower() == 'ah':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == 'hn':					
                    helpN = helpn()
                    cl.sendMessage(to, str(helpN))
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[群組列表]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower().startswith("gc "):
                    x = text.split(" ")
                    if x[1] in ban["user"]:
                        cl.sendMessage(to,"你還擁有{}張票".format(str(ban["user"][x[1]])))
                    else:
                        cl.sendMessage(to,"票不夠了。")
                elif text.lower() == '最高權限者':
                    if ban["owners"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ owners List ]"
                        for mi_d in ban["owners"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                elif text.lower() == '最高權限者mid':
                    if ban["owners"] == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "╔══[ owners List ]"
                        for mi_d in ban["owners"]:
                            mc += "\n╠ "+(mi_d)
                        cl.sendMessage(to,mc + "\n╚══[ Finish ]")							
                elif text.lower().startswith("踢 "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in ban["owners"]:
                            pass
                        else:
                            try:
                                kicker=random.choice([k1,k2,k3,k4])
                                kicker.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif text.lower() == 'kg':
                    gid = cl.getGroupIdsJoined() 
                    for i in gid:
                        group=cl.getGroup(i)
                        gMembMids = [contact.mid for contact in group.members] 
                        ban_list = [] 
                        for tag in ban["blacklist"]: 
                            ban_list += filter(lambda str: str == tag, gMembMids) 
                        if ban_list == []: 
                            cl.sendMessage(i, "沒有黑名單") 
                        else: 
                            for jj in ban_list: 
                                bot = random.choice([cl,k1,k2,k3,k4]) 
                                bot.kickoutFromGroup(i, [jj]) 
                            cl.sendMessage(i, "掃黑結束") 
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in ban["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to, "沒有黑名單")
                        else:
                            bot = random.choice([cl,k1,k2,k3,k4])
                            for jj in matched_list:
                                bot.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "黑名單以踢除")
                elif text.lower().startswith("add "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["admin"]:
                        ban["admin"].append(str(inkey))
                        cl.sendMessage(to, "已獲得權限！")
                    else:
                        cl.sendMessage(to,"already")
                elif text.lower().startswith("del "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["admin"]:
                        ban["admin"].remove(str(inkey))
                        cl.sendMessage(to, "已取消權限！")
                    else:
                    	cl.sendMessage(to,"user is not in admin")
                elif text.lower().startswith("godd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ban["owners"]:
                        ban["owners"].append(str(inkey))
                        cl.sendMessage(to, "已獲得作者權限！")
                    else:
                        cl.sendMessage(to,"已經在名單內")
                elif text.lower().startswith("godl "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ban["owners"]:
                        ban["owners"].remove(str(inkey))
                        cl.sendMessage(to, "已取消作者權限！")
                    else:
                     cl.sendMessage(to,"早就不再名單")
                elif text.lower() == 'ownerlist':
                    if ban["owners"] == []:
                        cl.sendMessage(msg.to,"NO owner")
                    else:
                         try:
                             mc = "[ owners名單 ]"
                             for mi_d in ban["owners"]:
                                 mc += "\n☞ " +cl.getContact(mi_d).displayName 
                             cl.sendMessage(msg.to,mc + "\n[ 已查完結果 ]")
                         except:
                             pass
                elif text.lower() == 'add':
                    wait["add"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'del':
                    wait["del"] = True
                    cl.sendMessage(to,"Please send a Contact")
                elif text.lower().startswith("a "):
                    x = text.split(" ")
                    ban["admin"].append(x[1])
                    if len(x) ==2:
                        if x[1] not in ban["user"]:
                            ban["user"][x[1]] = 1
                            cl.sendMessage(to,"ok")
                        else:
                            ban["user"][x[1]] +=1
                            cl.sendMessage(to,"ok")
                    elif len(x) ==3:
                        if x[1] not in ban["user"]:
                            ban["user"][x[1]] = int(x[2])
                            cl.sendMessage(to,"ok")
                        else:
                            ban["user"][x[1]] +=int(x[2])
                            cl.sendMessage(to,"ok")
                    backupData()
                elif text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] = True
                            cl.sendMessage(msg.to,"已加入黑單!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif text.lower().startswith("ban:"):
                    txt = text.replace("Ban:","")
                    try:
                        ban["blacklist"][txt] = True
                        cl.sendMessage(msg.to,"已加入黑單!")
                    except:
                        cl.sendMessage(msg.to,"添加失敗 !" +txt)
                elif text.lower().startswith("unban:"):
                    txt = text[6:].split(' ')
                    a = 0
                    for mid in txt:
                        try:
                            del ban["blacklist"][mid]
                            a+=1
                        except:
                            cl.sendMessage(msg.to,"刪除" + str(mid) + "失敗 !")
                    cl.sendMessage(msg.to,"已刪除黑單共" + str(a) + "人")
#==============================================================================#
                elif text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] =False
                            cl.sendMessage(msg.to,"刪除成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif text.lower() == 'ban':
                    wait["ban"] = True
                    cl.sendMessage(to,"Please send a contact")
                elif text.lower() == 'unban':
                    wait["unban"] = True
                    cl.sendMessage(to,"Please send a Contact")
#==============================================================================#
        if op.type == 25 or op.type ==26:
            msg = op.message
            if msg.contentType == 13:
                if wait["ban"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["blacklist"]:
                           cl.sendmessage(msg.to,"already")
                           wait["ban"] = False
                        else:
                           ban["blacklist"][msg.contentMetadata["mid"]] = True
                           wait["ban"] = False
                           cl.sendMessage(msg.to,"成功新增黑單")
                elif wait["unban"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["blacklist"]:
                           cl.sendmessage(msg.to,"already")
                           wait["unban"] = False
                        else:
                           del ban["blacklist"][msg.contentMetadata["mid"]]
                           wait["unban"] = False
                           cl.sendMessage(msg.to,"成功移除黑單")
                elif wait["add"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] in ban["admin"]:
                           cl.sendmessage(msg.to,"already")
                           wait["add"] = False
                        else:
                           ban["admin"].append(str(msg.contentMetadata["mid"]))
                           wait["add"] = False
                           cl.sendMessage(msg.to,"成功新增黑單")
                elif wait["del"] == True:
                    if msg._from in ban["owners"]:
                        if msg.contentMetadata["mid"] not in ban["admin"]:
                           cl.sendmessage(msg.to,"already")
                           wait["del"] = False
                        else:
                           ban["admin"].remove(str(msg.contentMetadata["mid"]))
                           wait["del"] = False
                           cl.sendMessage(msg.to,"成功移除黑單")
#                else:
#                    cl.sendMessage(msg.to,str(msg.contentMetadata["mid"]))
#==============================================================================#
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name	
                        sendMention(op.param1, "發現 @! 位成員默默已讀\n不要潛水  ",[op.param2])						
        if op.type == 26:
            try:
                msg = op.message
                if ban["reread"] == True:
                    if msg.toType == 2:
                        if msg.toType == 0:
                            cl.log("[%s]"%(msg._from)+msg.text)
                        else:
                            cl.log("[%s]"%(msg.to)+msg.text)
                        if msg.contentType == 0:
                            msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if ban["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[收回訊息人]\n%s\n[訊息內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
#==============================================================================#
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
