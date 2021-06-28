import boto3

bucketName="pictarrow-vietnam-public"

THUMBNAIL_DIR="D:/imageThumbnail/"

KEY_PREFIX="thumbnailSing+"

s3 = boto3.resource("s3", endpoint_url="http://192.168.34.102:4566", aws_access_key_id='', aws_secret_access_key='')

#get from database

imageIDs = ['973967', '737400', '613933', '593616', '307001', '221620', '75820', '45930']

imgPaths = [THUMBNAIL_DIR + x +"/" + x + ".jpg" for x in imageIDs]


for imid in imgPaths:
    print(imid)

bucket = s3.Bucket(bucketName)
#bucket.upload_file( Filename="D:/testenvi/221620.jpg", Key="testUpload/test.jpg" )

#bucket.download_file('testUpload/test.jpg', 'D:/testenvi/hello2.jpg')
