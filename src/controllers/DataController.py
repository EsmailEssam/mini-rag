from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal
import re
import os

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes

    
    def validate_upload_file(self, file: UploadFile):
        # check if the file type is supported
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        # check if the file size is within the allowed limit
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDS.value
        
        # return success
        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value
    
    def generate_unique_file_name(self, orig_file_name: str, project_id: str):
        
        # generate a random string
        random_string = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        # get the cleaned filename
        cleaned_filename = self.get_clean_filename(orig_file_name=orig_file_name)

        # generate the new file path
        new_file_path = os.path.join(
            project_path,
            f"{random_string}_{cleaned_filename}"
        )

        # check if the file path already exists
        while os.path.exists(new_file_path):
            random_string = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                f"{random_string}_{cleaned_filename}"
            )

        # return the new file path
        return new_file_path

    def get_clean_filename(self, orig_file_name: str):
        # remove all special characters except for . and _
        clean_filename = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # remove all spaces
        clean_filename = clean_filename.replace(' ', '')

        return clean_filename

