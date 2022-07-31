def checkAmstrong(n):
    amg=0
    temp=n
    while n>0:
        amg=amg+pow(n%10,3)
        n=n//10
    print(amg)
    if temp==amg :
        print("It is an amstrong number")
    else:
        print("It is not an amstrong number")
        # return amg
# Read Jason File using oy soark
from pyspark.sql import SparkSession

spark= SparkSession.builder.appName("test").master("local[3]").getOrCreate()
# print(spark.version)

spark.read.option("inferSchema",True).json("C:/Users/itsva/OneDrive/Desktop/Test1.json").show()




