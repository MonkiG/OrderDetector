from supabase import create_client, Client
from utils.config import config

url: str = config["SUPABASE_URL"]
key: str = config["SUPABASE_KEY"]

client: Client = create_client(url, key)
