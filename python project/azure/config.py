#-------------------------------------------------------------------------
# 
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, 
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES 
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
#----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
#--------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_quickstart_client.py "

_BATCH_ACCOUNT_NAME = 'iar'# Your batch account name
_BATCH_ACCOUNT_KEY = 'yi8Nb+x40Aku9LParQVBV4cKiBwuLROfNGUuDOFc6o4I2WuUzkoTi+DKYgXRaTQ2rfiX/BK6+RI4WOG1wy4Q0g==' # Your batch account key
_BATCH_ACCOUNT_URL = 'https://iar.francecentral.batch.azure.com/' # Your batch account URL
_STORAGE_ACCOUNT_NAME = 'iarstorage' # Your storage account name
_STORAGE_ACCOUNT_KEY = 'l5x07e0WlwzMlsmHo4KIDIU36N/xoFUAYcbEVyI+nQaBSf8qGkN8fYcUG4zD1r2goVINFJKP18b4gBCAePl4dg==' # Your storage account key
_POOL_ID = 'îar_pool' # Your Pool ID
_POOL_NODE_COUNT = 2 # Pool node count
_POOL_VM_SIZE = 'STANDARD_F1' # VM Type/Size
_JOB_ID = 'PythonMPIJob' # Job ID

_STANDARD_OUT_FILE_NAME = 'stdout.txt' # Standard Output file
_STANDARD_ERROR_FILE_NAME = 'stdout.txt' # Standard Error file