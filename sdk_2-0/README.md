# Tello SDK 2.0  

(September 2022) : Use Python 3.9.13  


---

## References  

- [SDK 2.0 UserGuide](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)  


- Python Sample  
  - [Tello3.py](https://dl-cdn.ryzerobotics.com/downloads/tello/20180222/Tello3.py)  


---

## SendCommand.py  

- Use Wi-Fi to establish a connection between the Tello and Device.  

- Start-up  
  `python SendCommand.py`  


---

## ReceiveState.py  

- Preparation  
  - Start `SendCommand.py`.  
  - Enter `command`.  


- Start-up  
  `python ReceiveState.py`  


---

## Emergency stop


### Windows  

- Get Process-ID  
  `tasklist | find "python"`  

- Shut down  
  `taskkill /f /pid (Process-ID)`  


---
