import urequests as requests
from rfid import read_rfid
import utime

firebase_database_url = "https://ogproject-afe3e-default-rtdb.europe-west1.firebasedatabase.app/"
private_key_path = "FUvHIJfTncqyqOgXtEt8Mk87nvKJPlu3OM5bdCmH"

# Connect to Wi-Fi

# Function to set data in Firebase
def set_data(key,data,collection_name):
    try:
        # Replace 'your_collection' with the specific collection you want to access
        firebase_url = f"{firebase_database_url}/{collection_name}/{key}.json"
        response = requests.post(firebase_url, json=data)
        if response.status_code == 200:
            pass
            #print("Data successfully set in Firebase")
        else:
            print("Failed to set data in Firebase. Status code:", response.status_code)
    except Exception as e:
        print("Error setting data:", e)
    finally:
        if response:
            response.close()


def get_data(collection_name):
    
    try:
        # Replace 'your_collection' with the specific collection you want to access
        firebase_url = f"{firebase_database_url}/{collection_name}.json"
        response = requests.get(firebase_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to get data from Firebase. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error getting data:", e)
        return None
    finally:
        if response:
            response.close()
            
            
            
def update_value_in_parks(field_to_update, new_value):
    try:
        firebase_url = f"{firebase_database_url}/Parks.json"
        response = requests.get(firebase_url)

        if response.status_code == 200:
            existing_data = response.json()

            if existing_data:
                # Update the specific field with the new value
                existing_data[field_to_update] = new_value

                # Send the updated data back to Firebase
                update_response = requests.put(firebase_url, json=existing_data)

                if update_response.status_code == 200:
                    pass
                   # print("Value successfully updated in Firebase")
                else:
                    print("Failed to update value in Firebase. Status code:", update_response.status_code)
            else:
                print("Document not found in Firebase.")
        else:
            print("Failed to fetch existing data. Status code:", response.status_code)
    except Exception as e:
        print("Error updating value:", e)
    finally:
        if response:
            response.close()
        if update_response:
            update_response.close()
            

            
def update_value_in_users(card_id,field_to_update, new_value):
    try:
        firebase_url = f"{firebase_database_url}/Users/{card_id}.json"
        response = requests.get(firebase_url)

        if response.status_code == 200:
            existing_data = response.json()

            if existing_data:
                # Update the specific field with the new value
                existing_data[field_to_update] = new_value

                # Send the updated data back to Firebase
                update_response = requests.put(firebase_url, json=existing_data)

                if update_response.status_code == 200:
                    pass
                   # print("Value successfully updated in Firebase")
                else:
                    print("Failed to update value in Firebase. Status code:", update_response.status_code)
            else:
                print("Document not found in Firebase.")
        else:
            print("Failed to fetch existing data. Status code:", response.status_code)
    except Exception as e:
        print("Error updating value:", e)
    finally:
        if response:
            response.close()
        if update_response:
            update_response.close()
            
            
# Example: Set data in Firebase
#data_to_set = {"name": "og", "CarId": "123" }
#set_data(1,data_to_set)

#print(check_date(data))

#while True :
 #   id1 = read_rfid()
  #  if id1 in data.keys():
   #     print(data[id1])
    #    print("high class")
    #else:
    #  print("hdddd")
    #utime.sleep(1)
