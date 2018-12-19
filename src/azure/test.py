# -*- coding: utf-8 -*-
import datetime

from azure.batch.models import ResourceFile
from azure.storage.blob import BlockBlobService, BlobPermissions

container_name = 'iarstoragev2'
block_blob_service = BlockBlobService(
    account_name=container_name,
    account_key='JfVlSA2HvGJxAiCXFGEzixeb7*****************************************Cif3F9YscCOcz4iKpvmg=='
)

generator = block_blob_service.list_blobs('input')
for blob in generator:
    sas_token = block_blob_service.generate_blob_shared_access_signature(
        container_name,
        blob.name,
        permission=BlobPermissions.READ,
        expiry=datetime.datetime.utcnow() + datetime.timedelta(hours=12))

    sas_url = block_blob_service.make_blob_url(
        container_name,
        blob.name,
        sas_token=sas_token)

    print(ResourceFile(file_path=blob.name, blob_source=sas_url))
