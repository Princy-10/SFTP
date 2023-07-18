import pysftp
import os
from sharepoint import SharePoint
from dotenv import load_dotenv
load_dotenv()
local_folder_path = "./LC"
sharepoint_folder_name ="19 June 2023"


### Change the path of Lyon   ####


SharePoint().upload_folder(local_folder_path, sharepoint_folder_name)