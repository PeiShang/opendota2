# opendota2 v0.1.0
- Author [PeiShang](https://github.com/PeiShang)
- The [OpenDota web api](https://docs.opendota.com/) in python
- [![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
## 1.Requirement
- Python version 3.0+
## 2.Download and install
- You can Clone the repository to your local machine via:
```shell
git clone git://github.com/PeiShang/opendota2
```
- Then cd to the folder and run:
```shell
pip install .
```
## 3.Usage
- You can import and use the pakages like:
```python
import opendota2 as od
match_data = od.get_match(match_id=3812844133) # Get the match data 
```
See the [OpenDota web api](https://docs.opendota.com/) for more information about parameters

