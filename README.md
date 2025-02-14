# Sky Plane Notifier

Check airplane schedules in a minimum time and get notified when the tickets are available at your desired price.

## How to contribute:
* Clone the project
* Create a venv (python virtual env) and activate it (*Optional but preferrable)
* Run in the project directory:
```powershell
pip install -r requirements.txt
```
* Change directory to src:
```shell
cd src/
```
* Run the python application:
```shell
uvicorn main:app --reload
```
* To test if the application is up, try consuming the **_health_** endpoint:
```powershell
curl localhost:3000/health
```