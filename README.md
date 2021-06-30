# Huriko
二重振り子の運動を数値計算するコード


![huriko](https://user-images.githubusercontent.com/42662735/115541580-4179be80-a2da-11eb-9ad3-0e973bc8dc09.gif)

## 概要
- `python`プロジェクトはpythonで書いた簡潔な二重振り子
- `multi_prescision`プロジェクトでは任意精度の浮動小数点数で数値計算できる

## 必要なもの
- GCC
- MPFR
- GMP
- python

## 使い方

### multi_precisionプロジェクト
```
cd multi_recision
g++ huriko.cpp -p huriko -lgmp -lmpfr
```

### pythonプロジェクト
```
cd python 
python huriko.py
```
