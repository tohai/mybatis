import boto3
import threading


numberimagerumathread = 2


bucketName="pictarrow-vietnam-public"

THUMBNAIL_DIR="D:/imageThumbnail/"

KEY_PREFIX="thumbnailSing/"

org1 = "_org_s1"
org2 = "_org_s2"
org3 = "_org_s3"

desTypefile = ".jpg"

class UploadTask(threading.Thread):
    def __init__(self,imgs):
        threading.Thread.__init__(self)
        self.imgs = imgs
    def run(self):
        # Here we create a new session per thread
        session = boto3.session.Session()

        # Next, we create a resource client using our thread's session object
        s3 = session.resource("s3", endpoint_url="http://192.168.34.102:4566", aws_access_key_id='', aws_secret_access_key='')
        bucket = s3.Bucket(bucketName)
        for img in self.imgs:
            orgkey = img + "/" + img + desTypefile
            orgkey1 = img + "/" + img+ org1 + desTypefile
            orgkey2 = img + "/" + img+ org2 + desTypefile
            orgkey3 = img + "/" + img+ org3 + desTypefile
            bucket.upload_file( Filename= THUMBNAIL_DIR + orgkey, Key=KEY_PREFIX+ orgkey )
            bucket.upload_file( Filename= THUMBNAIL_DIR + orgkey1, Key=KEY_PREFIX+ orgkey1 )
            bucket.upload_file( Filename= THUMBNAIL_DIR + orgkey2, Key=KEY_PREFIX+ orgkey2 )
            bucket.upload_file( Filename= THUMBNAIL_DIR + orgkey3, Key=KEY_PREFIX+ orgkey3 )

def numberThread (imgNum):
    if imgNum%numberimagerumathread == 0:
        return int(imgNum/numberimagerumathread)
    else:
        return int(imgNum/numberimagerumathread) + 1

def uploadImagesTos3(imgs):
    session = boto3.Session()
    s3 = session.resource("s3", endpoint_url="http://192.168.34.102:4566", aws_access_key_id='', aws_secret_access_key='')
    bucket = s3.Bucket(bucketName)
    for img in imgs:
        orgkey = img + "/" + img + desTypefile
        orgkey1 = img + "/" + img+ org1 + desTypefile
        orgkey2 = img + "/" + img+ org2 + desTypefile
        orgkey3 = img + "/" + img+ org3 + desTypefile
        bucket.upload_file( Filename= THUMBNAIL_DIR + orgkey, Key=KEY_PREFIX+ orgkey )
        bucket.upload_file( Filename= THUMBNAIL_DIR + orgkey1, Key=KEY_PREFIX+ orgkey1 )
        bucket.upload_file( Filename= THUMBNAIL_DIR + orgkey2, Key=KEY_PREFIX+ orgkey2 )
        bucket.upload_file( Filename= THUMBNAIL_DIR + orgkey3, Key=KEY_PREFIX+ orgkey3 )

    


#get from database

imageIDs = ['973967', '737400', '613933', '593616', '307001', '221620', '75820', '45930']

umberofthread = numberThread(len(imageIDs))
#print(umberofthread)
uploadImagesTos3(imageIDs)

#try:
#    for i in range(umberofthread):
#        if( i == umberofthread -1):
#            #print(umberofthread)
#            UploadTask(imageIDs[i*numberimagerumathread:]).start()
#        else:
#            #print(umberofthread)
#            UploadTask(imageIDs[i*numberimagerumathread:(i+1)*numberimagerumathread]).start()
#except:
#   print("Error: unable to start thread")
