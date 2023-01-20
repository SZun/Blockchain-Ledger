# PyChain Ledger

![Blockchain Image](./Resources/images/blockchain.png)

You’re a fintech engineer who’s working at one of the five largest banks in the world. You were recently promoted to act as the lead developer on their decentralized finance team. Your task is to build a blockchain-based ledger system, complete with a user-friendly web interface. This ledger should allow partner banks to conduct financial transactions (that is, to transfer money between senders and receivers) and to verify the integrity of the data in the ledger.

## The Application

Below is an image of the application in use. There is a form to record and submit the `Sender`, `Reciever` and `Amount` of the cryptocurrency. Below this we see a public ledger that along with the Genesis block, has recorded several other blocks for transactions. Below the ledger is a button to validate the chain. Once clicked, it will display `True` or `False` depending on the validity of the chain. In the image we see `True` in green text below the button, indicating that the chain is valid. On the left side of the application we see a slider to select the difficulty of tha chain's hash. Below this we have a dropdown to select a specific block from the chain ledger. And below that in green text we see the values of the block.

![App](./Resources/images/app.png)

### Chain Validation

Below we can see that the `Validate Chain` button has been pressed. Below the button we can see `True` in green text, which is an output signifying that the chain is valid.

![Ledger Verification](./Resources/images/ledger_verification.png)

### Block Inspector

Below we see that block inspector outputting the information for the block which were selected in the dropdown above it.

Satoshi Block             |  Vitalik Block
:-------------------------:|:-------------------------:
![Satoshi Block](./Resources/images/satoshi.png)  |  ![Vitalic Block](./Resources/images/vitalik.png)

## Getting Started
### Prerequisites

You must have Python 3 & Pip installed

```
$ python3 --version
Output: Python 3.10.8
$ pip --verison
Ouput: pip 22.2.2 from /Users/{#Username}/opt/anaconda3/lib/python3.9/site-packages/pip (python 3.9)
```

### Installing Dependencies

```
$ pip install pandas
$ pip install streamlit
```

### Clone Repository
```
$ git clone git@github.com:SZun/PyChain-Ledger.git
$ cd PyChain-Ledger
```

### Run The Application
```
$ streamlit run pychain.py
```

## Built With
[![Python 3.7.13](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)]([https://www.python.org/downloads/release/python-3713/)
[![Python](https://img.shields.io/badge/Python-3.7.13-blue)](https://www.python.org/downloads/release/python-3713/) - *Programming Language* <br>
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/) - *Web app generation tool* <br>
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/docs/#) - *Data analysis library*

### Python Libraries
- [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [hashlib](https://docs.python.org/3/library/hashlib.html)
- [typing](https://docs.python.org/3/library/typing.html)

## Contributors
- **Sam G. Zun** - [LinkedIn](https://www.linkedin.com/in/szun/) | [GitHub](https://github.com/SZun)