import json
import os
from datetime import datetime
from .exceptions import NotFoundException


class Storage:
    def __init__(self, name: str):
        self.file_path = self.create_file_if_not_exist(f"{name}.json")
        self.count_path = self.create_file_if_not_exist("count.txt")

    def create_file_if_not_exist(self, name: str):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        DIST_PATH = os.path.join(THIS_FOLDER, "dist")
        STORAGE_FILE_PATH = os.path.join(DIST_PATH, name)

        if not os.path.exists(DIST_PATH):
            os.makedirs(DIST_PATH)

        if not os.path.exists(STORAGE_FILE_PATH):
            with open(STORAGE_FILE_PATH, "w"):
                pass

        return STORAGE_FILE_PATH

    def insert(self, content) -> int:
        with open(self.file_path, "r+") as file, open(self.count_path, "r+") as count:
            try:
                storageJson = json.loads(file.read())
                prevId = count.read()
                id = int(prevId) + 1
                dict = {**content.__dict__, "id": id}
                updatedJson = {**storageJson, **{id: dict}}
                count.seek(0)
                count.truncate(0)
                count.write(str(id))
                file.seek(0)
                json.dump(updatedJson, file, default=str, indent=4)
            except Exception as e:
                id = 0
                count.seek(0)
                count.truncate(0)
                count.write(str(id))
                dict = {**content.__dict__, "id": id}
                json.dump({id: dict}, file, default=str, indent=4)

        return dict

    def update(self, id: str, content):
        with open(self.file_path, "r+") as file:
            try:
                storageJson = json.loads(file.read())
                if id not in storageJson:
                    raise NotFoundException
                updatedContent = {
                    **storageJson[id],
                    **content,
                    "updatedAt": datetime.now(),
                }
                storageJson[id] = updatedContent
                file.seek(0)
                file.truncate(0)
                json.dump(storageJson, file, default=str, indent=4)

                return updatedContent
            except Exception as e:
                raise e

    def delete(self, id: str):
        with open(self.file_path, "r+") as file:
            try:
                storageJson = json.loads(file.read())
                if id not in storageJson:
                    raise NotFoundException

                file.seek(0)
                file.truncate(0)
                removed = storageJson.pop(id)

                json.dump(storageJson, file, indent=4)

                return removed
            except Exception as e:
                raise e

    def find(self, id: str):
        with open(self.file_path, "r") as file:
            try:
                storageJson = json.loads(file.read())
                if id not in storageJson:
                    raise NotFoundException

                return storageJson[id]
            except Exception as e:
                raise e

    def find_all(self):
        with open(self.file_path, "r") as file:
            try:
                storageJson = json.loads(file.read())

                return storageJson
            except Exception as e:
                raise e
