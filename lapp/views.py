from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import pprint
from django.utils.datetime_safe import datetime
from django.contrib.auth import logout

from lapp.models import *
# Create your views here.

def main(request):

    return render(request,'loginindex.html')

def user_sign_up(request):
    return render(request,'registerindex.html')

def register(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    gender = request.POST['radio']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phone = request.POST['tel']
    email = request.POST['email']
    username = request.POST['uname']
    password = request.POST['password']
#to save it to database,crete a object assign it to the table.
    lob = login()
    lob.username = username
    lob.password= password
    lob.type = 'user'
    lob.save()
    uob = user()
    uob.fname = fname
    uob.lname = lname
    uob.gender = gender
    uob.place = place
    uob.post = post
    uob.pin = pin
    uob.phone = phone
    uob.email = email
    uob.lid=lob
    uob.save()
    return HttpResponse('''<script>alert("registered Successfully");window.location='user_sign_up'</script>''')

def log(request):
    username = request.POST['uname']
    password = request.POST['password']
    try:
        logOb = login.objects.get(username=username,password=password)
        if logOb.type == 'admin':
            request.session['lid'] = logOb.id  # store the login id session
            ob1=auth.authenticate(username='admin',password='admin') #for login authentication
            auth.login(request,ob1) #for login authentication
            return HttpResponse('''<script>alert("welcome admin");window.location='/adminHome'</script>''')
        elif logOb.type == 'agent':
            request.session['lid'] = logOb.id  # store the login id session
            ob1 = auth.authenticate(username='admin', password='admin') #for login authentication
            auth.login(request, ob1) #for login authentication
            return HttpResponse('''<script>alert("welcome agent");window.location='/agent_dashboard'</script>''')
        elif logOb.type == 'user':
            request.session['lid'] = logOb.id  # store the login id session
            ob1 = auth.authenticate(username='admin', password='admin') #for login authentication
            auth.login(request, ob1) #for login authentication
            return HttpResponse('''<script>alert("welcome user");window.location='/user_home'</script>''')
        else:
            return HttpResponse('''<script>alert("invalid username or password ");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("invalid username or password ");window.location='/'</script>''')

#admin
@login_required(login_url='/') #for login authentication
def adminHome(request):
    return render(request,'adminindex.html')

@login_required(login_url='/')
def add_and_manage_agent(request):
    agOb = agent.objects.all()
    return render(request,'Admin/AddAndManageAgent.html',{'val':agOb})

@login_required(login_url='/')
def deleteAgent(request,id):
    ob = agent.objects.get(lid__id=id)
    ob.delete()
    lob = login.objects.get(id=id)
    lob.delete()
    return HttpResponse('''<script>alert("agent deleted");window.location='add_and_manage_agent'</script>''')

@login_required(login_url='/')
def add_agent(request):
    return render(request,'Admin/ADD_AGENT.html')

@login_required(login_url='/')
def addAgent(request):
    name = request.POST['agentName']
    place = request.POST['agPlace']
    pin = request.POST['agPin']
    email = request.POST['agEmail']
    commision = request.POST['agentCommission']
    experience = request.POST['agentExp']
    username =request.POST['agUname']
    password = request.POST['agPass']
    lob = login()
    lob.username = username
    lob.password = password
    lob.type = 'agent'
    lob.save()
    aob = agent()
    aob.name = name
    aob.place = place
    aob.pin = pin
    aob.email = email
    aob.experiance = experience
    aob.commission_rate = commision
    aob.lid = lob
    aob.save()
    return HttpResponse('''<script>alert("Agent added successfully");window.location='add_and_manage_agent'</script>''')

@login_required(login_url='/')
def editAgent(request,id):
    ob=agent.objects.get(id=id)
    request.session['aid']=id

    return render(request,'Admin/EditAgent.html',{'val':ob})

@login_required(login_url='/')
def updateAgent(request):
    name = request.POST['agentName']
    place = request.POST['agPlace']
    pin = request.POST['agPin']
    email = request.POST['agEmail']
    commision = request.POST['agentCommission']
    expirience = request.POST['agentExp']
    ob=agent.objects.get(id=request.session['aid'])
    ob.name = name
    ob.place = place
    ob.pin = pin
    ob.email = email
    ob.commision_rate = commision
    ob.experiance = expirience
    ob.save()
    return HttpResponse('''<script>alert("Agent updated successfully");window.location='/add_and_manage_agent'</script>''')


@login_required(login_url='/')
def block_unblock_agent(request):
    aob = agent.objects.all()
    return render(request,'Admin/BLOCK_UNBLOCK_AGENT.html',{'val':aob})

@login_required(login_url='/')
def blockAgent(request,id):
    ob = login.objects.get(id=id)
    ob.type = "blocked"
    ob.save()
    return HttpResponse('''<script>alert("Agent blocked");window.location='/block_unblock_agent'</script>''')

@login_required(login_url='/')
def unblockAgent(request,id):
    ob = login.objects.get(id=id)
    ob.type = "agent"
    ob.save()
    return HttpResponse('''<script>alert("Agent unblocked");window.location='/block_unblock_agent'</script>''')

@login_required(login_url='/')
def send_reply(request,id):
    request.session['cid'] = id #take the id of the reply row
    return render(request,'Admin/SEND_REPLY.html')

@login_required(login_url='/')
def sendReply(request):
    rply = request.POST['textarea']
    ob = complaint.objects.get(id=request.session['cid'])
    ob.reply = rply
    ob.save()
    return HttpResponse('''<script>alert("reply sent");window.location='view_comp_send_rep'</script>''')

@login_required(login_url='/')
def view_comp_send_rep(request):
    compOb = complaint.objects.all()
    return render(request,'Admin/VIEW_COMP_SEND_REPLY.html',{'val':compOb})

@login_required(login_url='/')
def view_user(request):
    uob = user.objects.all()
    return render(request,'Admin/ViewUser.html',{'val':uob})

#Agent
@login_required(login_url='/')
def add_manage_policy(request):
    pob = policy.objects.all()
    return render(request,'Agent/ADD_MANAGE_POLICY.html',{'val':pob})

@login_required(login_url='/')
def add_policy(request):
    # uob = user.objects.all()
    return render(request,'Agent/Add_policy.html')   #,{'val':uob})

@login_required(login_url='/')
def addPolicy(request):
    # username = request.POST['select']
    policyNo = request.POST['policyNo']
    startDate = request.POST['sDate']
    endDate = request.POST['eDate']
    premAmount = request.POST['amount']
    commission = request.POST['comm']
    pob = policy()
    pob.policyNo = policyNo
    pob.start_date = startDate
    pob.end_date = endDate
    pob.premium_amount = premAmount
    pob.commission = commission
    pob.aid = agent.objects.get(lid__id=request.session['lid'])
    # pob.uid = username
    pob.save()
    return HttpResponse('''<script>alert("Policy added successfully");window.location='add_manage_policy'</script>''')

@login_required(login_url='/')
def editPolicy(request,id):
    eob = policy.objects.get(id=id)
    request.session['eid'] = id
    return render(request,'Agent/EditPolicy.html',{'val':eob})

@login_required(login_url='/')
def updatePolicy(request):
    plcyNo = request.POST['policyNo']
    strtDate = request.POST['sDate']

    endDate = request.POST['eDate']
    amount = request.POST['amount']
    commision = request.POST['comm']
    ob = policy.objects.get(id=request.session['eid'])
    ob.policyNo = plcyNo
    ob.start_date = strtDate
    ob.end_date = endDate
    ob.premium_amount = amount
    ob.commission = commision
    ob.save()
    return HttpResponse('''<script>alert("Policy updated ");window.location='add_manage_policy'</script>''')


@login_required(login_url='/')
def delPolicy(request,id):
    ob = policy.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Policy deleted");window.location='add_manage_policy'</script>''')

@login_required(login_url='/')
def agent_dashboard(request):
    return render(request,'agentindex.html')

@login_required(login_url='/')
def view_doubt_snd_rep(request):
    dbtOb = doubt.objects.all()
    return render(request,'Agent/VIEW_DBT_SND_REP.html',{'val':dbtOb})

@login_required(login_url='/')
def doubt_reply(request,id):
    request.session['did'] = id
    return render(request,'Agent/DOUBT_REPLY.html')

@login_required(login_url='/')
def doubtReply(request):
    rply = request.POST['textarea']
    ob = doubt.objects.get(id=request.session['did'])
    ob.reply = rply
    ob.save()
    return HttpResponse('''<script>alert("reply sent");window.location='view_doubt_snd_rep'</script>''')



@login_required(login_url='/')
def view_feed_rating(request):
    fedOb = feedback.objects.all()
    return render(request,'Agent/VIEW_FEED_RATING.html',{'val':fedOb})

@login_required(login_url='/')
def view_req_updt_stat(request):
    reqOb = user_request.objects.all()
    return render(request,'Agent/VIEW_REQ$UPDATE_STAT.html',{'val':reqOb})

@login_required(login_url='/')
def approve(request,id):
    ob = user_request.objects.get(id=id)
    ob.status = 'approved'
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("approved");window.location='/view_req_updt_stat'</script>''')

@login_required(login_url='/')
def reject(request,id):
    ob = user_request.objects.get(id=id)
    ob.status = 'rejected'
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location='/view_req_updt_stat'</script>''')



#User
@login_required(login_url='/')
def user_home(request):
    return render(request,'userindex.html')

@login_required(login_url='/')
def send_comp_view_rep(request):
    cob = complaint.objects.all()
    return render(request,'Users/SND_COMP_VIEW_REP.html',{'val':cob})

@login_required(login_url='/')
def send_dbt_view_rep(request):
    dob = doubt.objects.all()
    return render(request,'Users/SND_DBT_VIEW_REP.html',{'val':dob})

@login_required(login_url='/')
def send_comp(request):
    return render(request,'Users/SEND_COMP.html')
@login_required(login_url='/')
def sendComp(request):
    comp = request.POST['textarea']
    ob = complaint()
    ob.uid = user.objects.get(lid__id=request.session['lid'])
    ob.complaint = comp
    ob.reply = 'pending'
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("complaint sent");window.location='/send_comp_view_rep'</script>''')
@login_required(login_url='/')
def send_dbt(request):
    aob = agent.objects.all()
    return render(request,'Users/SEND_DOUBT.html',{'val':aob})
@login_required(login_url='/')
def sendDbt(request):
    dbt = request.POST['textarea']
    agnt = request.POST['select']
    ob = doubt()
    ob.uid = user.objects.get(lid__id=request.session['lid'])
    ob.aid = agent.objects.get(id=agnt)
    ob.doubt = dbt
    ob.reply = 'pending'
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("doubt sent");window.location='/send_dbt_view_rep'</script>''')

@login_required(login_url='/')
def send_feed_rating(request):
    aob = agent.objects.all()
    return render(request,'Users/SND_FEED_RATING.html',{'val':aob})

@login_required(login_url='/')
def sendFeedRating(request):
    feed = request.POST['textarea']
    agnt = request.POST['select']
    rating = request.POST['select2']
    ob = feedback()
    ob.uid = user.objects.get(lid__id=request.session['lid'])
    ob.aid = agent.objects.get(id=agnt)
    ob.feedback = feed
    ob.rating = rating
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("feedback sent");window.location='/send_feed_rating'</script>''')

@login_required(login_url='/')
def view_plcy_snd_req(request):
    pob = policy.objects.all()
    return render(request,'Users/VIEW_PLCY_SND_REQ.html',{'val':pob})

@login_required(login_url='/')
def sendplcyreq(request,id):
    ob=user_request()
    ob.pid=policy.objects.get(id=id)
    ob.uid = user.objects.get(lid__id=request.session['lid'])
    ob.date = datetime.today()
    ob.status = 'pending'
    ob.save()
    return HttpResponse('''<script>alert("request sent");window.location='/view_plcy_snd_req'</script>''')




@login_required(login_url='/')
def view_req_stat(request):
    reqOb = user_request.objects.all()
    return render(request,'Users/VIEW_REQ_STAT.html',{'val':reqOb})

@login_required(login_url='/')
def add_manage_file(request):
    fob = files.objects.all()
    return render(request,'Agent/Add_manageFiles.html',{'val':fob})

@login_required(login_url='/')
def addFiles(request):
    return render(request,'Agent/add_files.html')

@login_required(login_url='/')
def add_files(request):
    img = request.FILES['fileField']
    Fp = FileSystemStorage() #for storage
    Fs = Fp.save(img.name,img) #to save
    ob = files()
    ob.aid = agent.objects.get(lid__id=request.session['lid'])
    ob.file = Fs
    ob.date = datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("File added");window.location='/add_manage_file'</script>''')

@login_required(login_url='/')
def delFiles(request,id):
    ob = files.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("File deleted");window.location='/add_manage_file'</script>''')

@login_required(login_url='/')
def editFiles(request,id):
    fob = files.objects.get(id=id)
    request.session['fid'] = id
    return render(request,'Agent/EditFile.html',{'val':fob})

@login_required(login_url='/')
def updateFile(request):
    file = request.FILES['fileField']
    Fp = FileSystemStorage()  # for storage
    Fs = Fp.save(file.name, file)  # to save
    ob = files.objects.get(id=request.session['fid'])
    ob.file = Fs
    ob.save()
    return HttpResponse('''<script>alert("File updated ");window.location='/add_manage_file'</script>''')


def logout_view(request):
    auth.logout(request)
    return redirect('/')
