from dataclasses import dataclass
import aiofiles

import ujson as json


class Var:
    token: str

    def __init__(self):
        self.token = str()

    async def set_var_from_file(self, path: str) -> None:
        async with aiofiles.open(path, "rb") as  file:
            json_var = json.loads(await file.read())
            self.token = json_var["bot"]["token"]
