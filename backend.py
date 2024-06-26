API_KEY = "cc100f25af24b9f6a22eea3d77eec6cb"
import requests

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    nr_values = 8 * forecast_days
    filtered_data = data["list"][:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="florida", forecast_days=1, kind="Temperature"))