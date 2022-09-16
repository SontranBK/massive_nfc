# ***Massive NFC Desktop*** - an product for massive NFC card writing and reading

## 1. Getting Started
This project is an product for massive NFC card writing and reading, build on PC desktop (MacOS, Windows, Linux based OS). Until Sep 2022, we support Duali DE-950 and AB Circle CIR315A, CIR315B NFC reader. The product is mainly written in Python. 
## 2. Updates and releases!!!
* 【Sep 16, 2022】 version 1.0.0 (first version)
## 3. Reproducing process
3.1. Install required deps and libs

3.2. Please run application.py by typing in *terminal/shell* as instructed below: 
- If you are on Linux, MacOS
```shell
python3 application.py
```
- If you are on Windows:
```shell
python application.py
```

## 4. Developing detail
### 4.1. Tools and docs
- For AB Circle and DE-950 read, write test files, refer to [this folder](TestFiles_ignored)
- AB Circle and DE-950 protocol included in [this folder](Tools_And_Docs/Protocols_DevGuide)
- For manually write NFC card (now massively), refer to [this folder](Tools_And_Docs/Massive_Write_Card)
### 4.2. Other info:
- Written by Python3. Also, pythonQT5, pandas, pyserial, pyscard and other libs required
- Runnable on every python3-supported platform and OS (Linux, Windows, MacOS)
- Already tested on Raspberry Pi 4 2GB, any devices with more specs (CPU, GPU, RAM) is runnable.
- Now support Duali DE-950, AB Circle CIR315A, CIR315B NFC reader
## 5. Authors and credits:
In research and development process, all credits go to ***Son Tran BK and CTARG LAB members***, in EEE, HUST (Hanoi University of Science and Technology), Ha Noi, Viet Nam

