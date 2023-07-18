import pysftp
import os
from sharepoint import SharePoint
from dotenv import load_dotenv
load_dotenv()


sftpHost = 'ec2-3-138-155-135.us-east-2.compute.amazonaws.com'
sftpPort = 22  
un = os.getenv("uname")
pawd = os.getenv("pawd")
cnOpts =pysftp.CnOpts()
cnOpts.hostkeys = None

with pysftp.Connection(host=sftpHost, port=sftpPort, username=un, password=pawd, cnopts=cnOpts) as sftp:
    print("connected")
    print(pawd)
    sftp.get("/limestone/ToVirtue/InquiryDataFile_20230717.csv", localpath="./tmp/InquiryDataFile_20230717.csv", preserve_mtime=True)
    sftp.get("/limestone/ToVirtue/FinancialAidDataFile_20230717.csv", localpath="./tmp/FinancialAidDataFile_20230717.csv", preserve_mtime=True)
    sftp.get("/limestone/ToVirtue/AdmissionsDataFile_20230717.csv", localpath="./tmp/AdmissionsDataFile_20230717.csv", preserve_mtime=True)

local_folder_path = "./tmp"
sharepoint_folder_name ="17 July 2023"

SharePoint().upload_folder(local_folder_path, sharepoint_folder_name)
