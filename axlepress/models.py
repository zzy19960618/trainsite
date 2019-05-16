from django.db import models

# Create your models here.


class RawData(models.Model):
    num1 = models.SmallIntegerField()
    num2 = models.SmallIntegerField()
    num3 = models.SmallIntegerField()
    num4 = models.SmallIntegerField()
    num5 = models.SmallIntegerField()
    num6 = models.SmallIntegerField()
    num7 = models.SmallIntegerField()
    num8 = models.SmallIntegerField()

    def __str__(self):
        return str(self.num1) + " " + str(self.num2) + " " + str(self.num3) + " " + str(self.num4) + " " + str(self.num5) + " " + str(self.num6) + " " + str(self.num7) + " " + str(self.num8)

    class Meta:
        verbose_name = "原始数据"
        verbose_name_plural = "原始数据"


class Train(models.Model):
    trainNo = models.CharField(max_length=10, primary_key=True)
    startP = models.CharField(max_length=10)
    endP = models.CharField(max_length=10)
    startT = models.DateTimeField()
    endT = models.DateTimeField()
    use = models.FloatField()

    def __str__(self):
        return self.trainNo + " " + str(self.startT) + " to " + str(self.endT)

    class Meta:
        verbose_name = "车次管理"
        verbose_name_plural = "车次管理"
        ordering = ['startT']


class Carriage(models.Model):
    carriageNo = models.SmallIntegerField(primary_key=True)
    comment = models.CharField(max_length=100)
    use = models.FloatField()

    def __str__(self):
        return self.carriageNo + " " + self.comment

    class Meta:
        verbose_name = "车厢管理"
        verbose_name_plural = "车厢管理"
        ordering = ['carriageNo']


class TrainCarriage(models.Model):
    trainNo = models.ForeignKey(Train, on_delete=models.DO_NOTHING, verbose_name="train_No")
    carriageNo = models.ForeignKey(Carriage, to_field="carriageNo", on_delete=models.DO_NOTHING, verbose_name="carriage_No")
    startT = models.DateTimeField()

    def __str__(self):
        return self.trainNo

    class Meta:
        verbose_name = "车次车厢配置"
        verbose_name_plural = "车次车厢配置"
        ordering = ['trainNo']


class CarAxle(models.Model):
    carriageNo = models.ForeignKey(Carriage, on_delete=models.DO_NOTHING, verbose_name="车厢")
    axleNo = models.CharField(max_length=1)

    def __str__(self):
        return self.carriageNo.carriageNo + "  " + str(self.axleNo)

    class Meta:
        verbose_name = "车厢车轴配置"
        verbose_name_plural = "车厢车轴配置"
        ordering = ['carriageNo', 'axleNo']


class Pressure(models.Model):
    time = models.DateTimeField()               #id外键引用
    millisec = models.IntegerField()
    axle1_pressure = models.SmallIntegerField()
    axle2_pressure = models.SmallIntegerField()
    axle3_pressure = models.SmallIntegerField()
    axle4_pressure = models.SmallIntegerField()
    rawData = models.ForeignKey(RawData,on_delete=models.DO_NOTHING)
    carAxle = models.ForeignKey(CarAxle,on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Car_axle_ID: " + str(self.carAxle) + " " + str(self.time) +" " + str(self.millisec) + " 1点压力:" + str(self.axle1_pressure)+ " 2点压力:" + str(self.axle2_pressure)+ " 3点压力:" + str(self.axle3_pressure)+ " 4点压力:" + str(self.axle4_pressure)

    class Meta:
        verbose_name = "车轴压力"
        verbose_name_plural = "车轴压力"
        ordering = ['carAxle']
