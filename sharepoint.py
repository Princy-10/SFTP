from shareplum import Site, Office365
from shareplum.site import Version
import os
from dotenv import load_dotenv
load_dotenv()



USERNAME = os.getenv("user")
PASSWORD = os.getenv("password")
SHAREPOINT_URL = os.getenv("url")
SHAREPOINT_SITE = os.getenv("site")
SHAREPOINT_DOC =os.getenv("doc_library")

print(SHAREPOINT_DOC)
class SharePoint:
    def auth(self):
         self.authcookie = Office365(SHAREPOINT_URL, username=USERNAME, password=PASSWORD).GetCookies()
         self.site = Site(SHAREPOINT_SITE, version=Version.v365, authcookie=self.authcookie)
         return self.site  
        
    def connect_folder(self, folder_name ):
         self.auth_site = self.auth()
         self.sharepoint_dir = '/'.join([SHAREPOINT_DOC, folder_name])
         self.folder = self.auth_site.Folder(self.sharepoint_dir)
         return self.folder

    def upload_folder(self, local_folder_path, folder_name , timeout =(100,200)):
        self._folder = self.connect_folder(folder_name)
        for filename in os.listdir(local_folder_path):
            file_path = os.path.join(local_folder_path, filename)
            with open(file_path, "rb") as file_obj:
                file_content = file_obj.read()
            self._folder.upload_file(file_content, filename)  
                