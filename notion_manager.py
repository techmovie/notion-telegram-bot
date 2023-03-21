from notion_client import Client
from config import NOTION_API_KEY, NOTION_DATABASE_ID
from logger import logger

class NotionManager:
    def __init__(self):
        self.notion = Client(auth=NOTION_API_KEY)
        self.default_database_id = NOTION_DATABASE_ID

    def get_database_properties(self,database_id = None):
        if database_id is None:
            database_id = self.default_database_id
        database = self.notion.databases.retrieve(database_id)
        return database["properties"]

    def _get_database_id(self, message):
        lines = message.split('\n')
        for line in lines:
            if line.startswith('database_id:'):
                return line.split('database_id:')[1].strip()
        return self.default_database_id
    
    def get_database_properties(self, database_id):
      database = self.notion.databases.retrieve(database_id)
      return database["properties"]
    
    def parse_message(self, message):
        data = {}
        lines = message.split('\n')
        for line in lines:
            if ':' in line:
                prop_name, value = line.split(':', 1)
                data[prop_name] = value
        return data

    def add_to_database(self, message):
        try:
            database_id = self._get_database_id(message)
            properties = self.get_database_properties(database_id)
            data = self.parse_message(message)
            if not properties:
                raise BaseException(f"The properties of database {database_id} is empty.Please check the database and try again.")
            if not data:
                raise ValueError("The parsed message is empty. Please check the message format.")
            
            unrecognized_properties = []
            new_page = {}
            for key, value in data.items():
                if key in properties:
                    new_page[key] = self.create_property_value(properties[key]['type'], value)
                elif(key != "database_id"):
                    unrecognized_properties.append(key)
            if unrecognized_properties:
                 raise ValueError(f"The following keys are not present in the database properties: {', '.join(unrecognized_properties)}. Please check the property names and try again.")
            if not new_page:
                raise ValueError("The provided property is empty. Please check the message format.")
            self.notion.pages.create(parent={"database_id": database_id}, properties=new_page)
        except ValueError as ve:
            raise ve
        except Exception as e:
             raise e
       
    def create_property_value(self, property_type, value):
      if property_type == "title":
          return {"title": [{"text": {"content": value}}]}
      elif property_type == "rich_text":
          return {"rich_text": [{"text": {"content": value}}]}
      elif property_type == "number":
          return {"number": float(value)}
      elif property_type == "select":
          return {"select": {"name": value}}
      elif property_type == "multi_select":
          return {"multi_select": [{"name": v.strip()} for v in value.split(',')]}
      elif property_type == "date":
          return {"date": {"start": value}}
      elif property_type == "people":
          # This example assumes that user input is a comma-separated list of user IDs.
          return {"people": [{"id": user_id.strip()} for user_id in value.split(',')]}
      elif property_type == "files":
          # This example assumes that user input is a comma-separated list of file URLs.
          return {"files": [{"external": {"url": file_url.strip()}} for file_url in value.split(',')]}
      elif property_type == "checkbox":
          return {"checkbox": value.lower() == 'true'}
      elif property_type == "url":
          return {"url": value}
      elif property_type == "email":
          return {"email": value}
      elif property_type == "phone_number":
          return {"phone_number": value}
      else:
          raise ValueError(f"Unsupported property type: {property_type}")
