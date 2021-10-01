import boto3

def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def list_files(bucket):
    s3_client = boto3.client('s3')
    contents = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            # print(item)
            contents.append(item)
    except Exception as e:
        pass
    return contents

def show_image(bucket):
    s3_client = boto3.client('s3')
    # location = boto3.client('s3').get_bucket_location(Bucket=bucket)['LocationConstraint']
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
            # print("[DATA] : presigned url = ", presigned_url)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    # print("[DATA] : The contents inside show_image = ", public_urls)
    return public_urls
    
def list_bucket():
    bucketreturn = []
    s3 = boto3.resource('s3')
    pattern = '.+lab.+(img\-mgr|imgmgr).+'
    buckets = s3.buckets.all()
    for b in buckets:
        if re.match(pattern, b.name):
            bucketreturn.append(b.name)
    return bucketreturn

def filter_bucket(bucketList):
    if bucketList == []:
        return None
    else:
        try:
            bucketList.count(0)
            return bucketList[0]
        except:
            return bucketList

def create_bucket():
    s3 = boto3.resource('s3')
    bucketuuid = str(uuid.uuid4()).split('-')[-1]
    bucketname = 'top-lab-imgmgr-' + bucketuuid
    s3.create_bucket(Bucket=bucketname)
