# Final-Report-Selenium

### Website : https://nhanvan.vn/

### Test Cases Manual : https://docs.google.com/spreadsheets/d/15JI9ma6HdpQmdbwhCUzVP3ujO8iiQbgd/edit?usp=sharing&ouid=100499490863982465973&rtpof=true&sd=true

### Project Report : https://docs.google.com/document/d/1LmMcX2ZmzTCnPe7JpjZZK8qasg_z_EOn/edit?usp=sharing&ouid=117418363728260771379&rtpof=true&sd=true



## Demo

<p align="center">
  <img width="700" align="center" src="https://github.com/AnhTan1420/Final-Report-Selenium/blob/main/Demo_Doan.gif" alt="demo"/>
</p>

## How to install 
### Install Project 

```
 git clone https://github.com/AnhTan1420/Final-Report-Selenium.git
```

### Activate .venv
#### Mac/Linux
```
 source .venv/bin/activate
```
#### Window
```
.venv/Scripts/activate
```

### Install requirements.txt

```
 pip3 install -r requirements.txt 
```

## How to run
### Edit Data Excel
![image](https://user-images.githubusercontent.com/58280404/233416297-c0b590f0-145f-41a7-a4b9-66c9fa85acbd.png)


### Run Each Case
```
 pytest -sv src/tests/test_register.py
```

### Run Entire Case
```
 pytest -sv src/tests/test_*.py
```