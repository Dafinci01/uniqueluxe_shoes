from fastapi import APIROUTER, HTTPExcetion, Query, Depends
from app.services.general_services import (
    save_contact_message,
    search_products, 

)