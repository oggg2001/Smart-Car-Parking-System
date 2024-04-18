from  firebase import get_data, set_data
def get_existing_indices(id):
    try:
            return [Users.get("parking_index", None) for Users in data.values() if "parking_index" in Users]
        else:
            print("Failed to fetch data. Status code:", response.status_code)
    except Exception as e:
        print("Error fetching data:", e)
    finally:
        if response:
            response.close()