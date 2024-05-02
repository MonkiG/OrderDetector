from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "SUPABASE_URL": os.environ.get("SUPABASE_URL"),
    "SUPABASE_KEY": os.environ.get("SUPABASE_KEY"),
    "AWS_REGION": os.environ.get("AWS_REGION"),
}
