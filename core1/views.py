from django.db import OperationalError
from django.shortcuts import render

# import requests
import requests
# For read json
import json
# Generating tokkens
import uuid



def engine(request):
    try:
        # Creating random token id
        token_id = uuid.uuid4()
        
        # Getting template data
        reg = request.POST.get('name')
        # Retrieving data from the external API
        try:
            url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
            data = {"registrationNumber": reg}
            headers = {'x-api-key': '7TUL5z8I1t4M12xIxDJVE9wkQjDB4tB5RlnlYGk5', 'Content-Type': 'application/json'}
            response = requests.post(url, headers=headers, data=json.dumps(data))
        except:
            response.raise_for_status()  # Raise HTTPError for bad responses
        # Convert response to JSON
        car_info = response.json()
        # Check if the car with the given registration number already exists
        
        {
        'tokken_id': token_id,
        'name': car_info.get('make', ''),
        'year': car_info.get('yearOfManufacture', ''),
        'engine': car_info.get('engineCapacity', ''),
        }
        
        
    except Exception as e:
        print(e)


def packages(request):
    
    return render(request, "core1/packages.html")