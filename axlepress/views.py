from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConfigTrainForm
from .models import Train
from .models import Carriage
from .models import TrainCarriage
from django.contrib import messages
from django.utils.safestring import mark_safe
import pandas as pd
import os
import time,datetime
import pymysql
pymysql.install_as_MySQLdb()
import numpy as np
import math
import cmath



# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def test(request):
    # print(os.path.abspath(__file__))
    # print(os.path.dirname(os.path.abspath(__file__)))
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    pass

def index(request):
    return render(request, 'showdata.html', {'prompt':'true'})


def getData(request):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='test',
        charset='utf8'
    )
    cursor = conn.cursor()
    trainNo = request.POST['trainNo']
    carriageNo = request.POST['carriageNo']
    axleNo = request.POST['axleNo']
    duration = request.POST['duration']
    beginTime=""
    lasttime=""
    promptinfo="true"
    #print('duration------------',duration)

    radio = request.POST['radiobutton']
    #print('radio--------', radio)
    wradio1 = ""
    wradio2 = ""
    if radio == '1':
        wradio1 = 'false'
        wradio2 = 'true'
        beginTime = request.POST['beginDateTime']
        if len(duration):
            timeArray = time.strptime(beginTime, "%Y-%m-%dT%H:%M:%S")
            timeStamp = int(time.mktime(timeArray))
            lastStamp = timeStamp + int(duration)
            lastArray = time.localtime(lastStamp)
            lasttime = time.strftime("%Y-%m-%dT%H:%M:%S", lastArray)
            print('beginTime--------------', timeStamp)
            print('lasttime1------------', lasttime)
        else:
            lasttime = request.POST['lastDateTime']
    else:
        wradio1 = 'true'
        wradio2 = 'false'
        radio = '0'
        if len(duration):
            timeStamp=time.time()
            beginTimeArray=time.localtime(timeStamp)
            beginTime=time.strftime("%Y-%m-%dT%H:%M:%S",beginTimeArray)
            lastStamp=timeStamp - int(duration)
            lastArray = time.localtime(lastStamp)
            lasttime = time.strftime("%Y-%m-%dT%H:%M:%S", lastArray)
            middletime=beginTime
            beginTime=lasttime
            lasttime=middletime
        else:
            messages.success(request,"请输入秒数")

    carriage = ""
    carriage1 = ""
    trainid = ""
    trainid1 = ""
    traincarriage = ""
    traincarriage1 = ""
    caraxle = ""
    caraxle1 = ""
    a1 = ""
    b1 = ""
    c1 = ""
    d1 = ""
    e1 = ""
    xdata=""

    trainid = cursor.execute('select * from axlepress_train where trainNo="' + trainNo + '"')
    trainid1 = list(((row[0] for row in cursor.fetchall())))
    print('trainid1:', list(trainid1))
    if len(trainid1):
        #print("trainid非空")
        carriageid = cursor.execute('select * from axlepress_carriage where carriageNo="' + carriageNo + '"')
        carriageid1 = list(((row[0] for row in cursor.fetchall())))
        print('carriageid1:', list(carriageid1))
        if len(carriageid1):
            #print("carriageid非空")
            axleid = cursor.execute('select * from axlepress_caraxle where axleNo="' + axleNo + '"')
            axleid1 = list(((row[0] for row in cursor.fetchall())))
            print('axleid1:', list(axleid1))
            if len(axleid1):
                #print("axleid非空")
                traincarriage = cursor.execute(
                    'select carriageNo_id from axlepress_traincarriage where (trainNo_id="' + trainNo + '" and carriageNo_id="' + carriageNo + '")')
                traincarriage1 = list(((row[0] for row in cursor.fetchall())))
                print("traincarriage:", traincarriage1)
                if len(traincarriage1):
                    #print("车次号和车厢号对应")
                    caraxle = cursor.execute('select id from axlepress_caraxle where carriageNo_id="' + carriageNo + '"')
                    caraxle1 = list(((row[0] for row in cursor.fetchall())))
                    print("caraxle1:", caraxle1)
                    if len(caraxle1):
                        #print("车厢号和车轴号对应")
                        a_sql =  'select time from axlepress_pressure where time between "' + beginTime + '" and "' + lasttime + '"'
                        a_time = pd.read_sql(a_sql, conn)
                        xdata = list(a_time["time"].values.tolist())
                        print("-----------------------------xdata-------------------------------------")
                        print("时间:", xdata)
                        if len(xdata):
                            b = cursor.execute(
                                'select axle1_pressure from (select * from axlepress_pressure order by id desc) a where carAxle_id="' + axleNo + '" and time between "' + beginTime + '" and "' + lasttime + '" order by id')
                            b1 = ((row[0] for row in cursor.fetchall()))
                            c = cursor.execute(
                                'select axle2_pressure from (select * from axlepress_pressure order by id desc) b where carAxle_id="' + axleNo + '" and time between "' + beginTime + '" and "' + lasttime + '" order by id')
                            c1 = ((row[0] for row in cursor.fetchall()))
                            d = cursor.execute(
                                'select axle3_pressure from (select * from axlepress_pressure order by id desc) c where carAxle_id="' + axleNo + '" and time between "' + beginTime + '" and "' + lasttime + '" order by id')
                            d1 = ((row[0] for row in cursor.fetchall()))
                            e = cursor.execute(
                                'select axle4_pressure from (select * from axlepress_pressure order by id desc) d where carAxle_id="' + axleNo + '" and time between "' + beginTime + '" and "' + lasttime + '" order by id')
                            e1 = ((row[0] for row in cursor.fetchall()))
                            promptinfo = 'false'
                        else:
                            if radio=='1':
                                promtinfo='true'
                                print("该时间段内没有数据")
                                messages.success(request,"该时间段内没有数据")
                            else:
                                promtinfo='true'
                    else:
                        promtinfo = 'true'
                        print("车厢号和车轴号不对应")
                        messages.success(request, "车厢号和车轴号不对应")
                else:
                    promtinfo = 'true'
                    print("车次和车厢号不对应")
                    messages.success(request, "车次和车厢号不对应")
            else:
                promtinfo = 'true'
                print("axleid空")
                messages.success(request, "此车轴号不存在")
        else:
            promtinfo = 'true'
            print("carriageid空")
            messages.success(request, "此车厢号不存在")
    else:
        promtinfo = 'true'
        print("trainid空")
        messages.success(request, "此车次号不存在")

    ydata1 = list(b1)
    ydata2 = list(c1)
    ydata3 = list(d1)
    ydata4 = list(e1)
    maxValue = ""
    minValue=""
    avgValue1=""
    avgValue2=""
    avgValue3=""
    avgValue4=""
    num=""

    fourier1 =""
    fourier2 = ""
    fourier3 = ""
    fourier4 = ""
    fourierx1 = []
    fourierx2 = []
    fourierx3 = []
    fourierx4 = []
    fouriery1 = []
    fouriery2 = []
    fouriery3 = []
    fouriery4 = []
    maxfouriery1 = ""
    maxfouriery2 = ""
    maxfouriery3 = ""
    maxfouriery4 = ""

    if ydata1 and ydata2 and ydata3 and ydata4:
        value = [max(ydata1), max(ydata2), max(ydata3), max(ydata4)]
        maxValue = max(value)
        minValue=min([min(ydata1),min(ydata2),min(ydata3),min(ydata4)])
        avgValue1=np.mean(ydata1)
        avgValue2 = np.mean(ydata2)
        avgValue3 = np.mean(ydata3)
        avgValue4 = np.mean(ydata4)


        fourier1=np.fft.fft(ydata1)
        for index in range(len(fourier1)):
            x,y=cmath.polar(fourier1[index])
            fouriery1.insert(index,x)
        maxfouriery1=max(fouriery1)
        fourierx1=(np.fft.fftfreq(len(ydata1), 0.01)).tolist()
        print('fourierx1----',fourierx1)
                #
        fourier2 = np.fft.fft(ydata2)
        for index in range(len(fourier2)):
            x, y = cmath.polar(fourier2[index])
            fouriery2.insert(index, x)
        maxfouriery2 = max(fouriery2)
        fourierx2=(np.fft.fftfreq(len(ydata2), 0.01)).tolist()
        print('fourierx2----',fourierx2)

        fourier3 = np.fft.fft(ydata3)
        for index in range(len(fourier3)):
            x, y = cmath.polar(fourier3[index])
            fouriery3.insert(index,x)
        maxfouriery3 = max(fouriery3)
        print('fourierx3----',fourierx3)
        fourierx3=(np.fft.fftfreq(len(ydata3), 0.01)).tolist()

        fourier4 = np.fft.fft(ydata4)
        for index in range(len(fourier4)):
            x, y = cmath.polar(fourier4[index])
            fouriery4.insert(index, x)
        maxfouriery4 = max(fouriery4)
        fourierx4=(np.fft.fftfreq(len(ydata4), 0.01)).tolist()
        print('fourierx4----',fourierx4)

    else:
        if radio=='1':
            promptinfo='true'
            #messages.success(request, "查询失败")
        else:
            promptinfo='true'
    pageHtml1=mark_safe(beginTime)
    pageHtml2=mark_safe(lasttime)
    itemDict = {'xdata': xdata, 'ydata1': ydata1, 'ydata2': ydata2, 'ydata3': ydata3, 'ydata4': ydata4,
                'maxValue': maxValue,'wradio1':wradio1,'wradio2':wradio2,'radio':radio,
                'trainNo': trainNo, 'carriageNo': carriageNo, 'axleNo': axleNo, 'beginTime': pageHtml1,
                'lastTime': pageHtml2, 'interval': duration,'minValue':minValue,'avgValue1':avgValue1,
                'avgValue2':avgValue2,'avgValue3':avgValue3,'avgValue4':avgValue4,
                'fourierx1':fourierx1,'fouriery1':fouriery1,'maxfouriery1':maxfouriery1,
                'fourierx2':fourierx2,'fouriery2':fouriery2,'maxfouriery2':maxfouriery2,
                'fourierx3':fourierx3,'fouriery3':fouriery3,'maxfouriery3':maxfouriery3,
                'fourierx4':fourierx4,'fouriery4':fouriery4,'maxfouriery4':maxfouriery4,
                'promptinfo': promptinfo}
    print(itemDict)
    return render(request, 'showdata.html', itemDict)



def inquiry(request):
    trainNo = request.POST['queryTrainNo']
    carriageNo = request.POST['queryCarriageNo']
    startT = request.POST['queryStartT']
    endT = request.POST['queryEndT']
    return render(request, 'cfgtrain.html')


def cfgtrain(request):
    if (request.method == "POST"):
        trainNo = request.POST['trainNo']       #车次是key，不能重复。
        carriageNoList = request.POST['carriageNo'].split("\r\n")
        startP = request.POST['startP']
        endP = request.POST['endP']
        startT = request.POST['startT']
        endT = request.POST['endT']
        currrentT = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("trainNo:", trainNo)
        print("CarriageNo:", carriageNoList)
        print("startP:", startP)
        print("endP: %s" % endP)
        print("startT:", startT)
        print("endT:%d", endT)

        itemDict = {'trainNo':trainNo, 'carriageNo':request.POST['carriageNo'],"startP": startP, "endP": endP,  "startT": startT, "endT": endT, "currentTime":currrentT }

        #检查车次是否存在
        if Train.objects.filter(trainNo=trainNo).exists():
            itemDict['error'] = "输入的车次号重复！"
            return render(request, 'cfgtrain.html', itemDict)

        #检查车厢是否存在，todo：一次提示全部未录入的车厢。
        for carriage in carriageNoList:
            if Carriage.objects.filter(carriageNo=carriage).exists():
                continue
            else:
                if len( carriage.strip() ) == 0:
                    itemDict['error'] = '安排车次时，需输入挂载车厢的编号！'
                else:
                    itemDict['error'] = '车厢' + carriage + '不存在，请管理员增加车厢后再增加车次。'
                return render(request, 'cfgtrain.html', itemDict)

        #建立train记录
        train = Train(trainNo=trainNo, startP=startP, endP=endP, startT=startT, endT=endT)

        #建立车次与车厢的关系
        carriage_list = []
        for carriage in carriageNoList:
            carriageInstance = Carriage(carriageNo=carriage)
            carriage_list.append(TrainCarriage(trainNo=train, carriageNo=carriageInstance))

        #执行写操作
        train.save()
        TrainCarriage.objects.bulk_create(carriage_list)

        return render(request, 'cfgtrain.html', itemDict)

    else:
        return render(request, 'cfgtrain.html')


def configTrain(request):
    if request.method == "POST":
        cfg_form = ConfigTrainForm(request.POST)
        if cfg_form.is_valid():
            #处理数据保存到数据库中
            trainNo = cfg_form.cleaned_data['trainNo']
            startP = cfg_form.cleaned_data['startP']
            endP = cfg_form.cleaned_data['endP']
            startT = cfg_form.cleaned_data['startT']
            endT = cfg_form.cleaned_data['endT']
            carriageList = cfg_form.cleaned_data['carriageList']
            print("No:", trainNo,"Station: ", startP,endP,'Time:',startT,endT,'List',carriageList)
            return HttpResponse("The data has been received.")
        else:
            print(cfg_form.errors)
    else:
        cfg_form = ConfigTrainForm()

    return render(request, 'test.html', {'form': cfg_form})

