# 신용카드 사기 탐지 모델 비교 분석

## 📌 실험 개요

- 목표: 신용카드 거래 데이터에서 사기(Class=1)를 탐지하는 머신러닝 모델을 비교하여 더 효과적인 방법을 도출
- 데이터셋: Credit Card Fraud Detection (Kaggle)
- 실험 도구: MLFlow (v3.4.0)
- 비교 모델:
  - Logistic Regression
  - Random Forest Classifier

---

## ⚙️ 모델 성능 비교 (MLFlow 기준)

| 모델 | Accuracy | Precision | Recall |
|------|----------|-----------|--------|
| Random Forest | 1.000 | 0.942 | 0.827 |
| Logistic Regression | 0.999 | 0.827 | 0.633 |

- Accuracy: 두 모델 모두 거의 완벽한 정확도를 보임
- Precision: Random Forest가 0.942로 더 높은 정밀도
- Recall: Random Forest가 사기 거래를 더 잘 탐지 (0.827 vs 0.633)

---

## 🔍 분석 및 결론

- 불균형 데이터에서는 정확도(Accuracy)는 큰 의미가 없음  
  → 사기 거래는 전체 거래의 극소수이므로, Recall(재현율)과 Precision(정밀도)가 더 중요

- Random Forest는 Logistic Regression보다 전반적으로 뛰어난 성능을 보였음  
  → 특히 Recall이 높아 실제 사기 탐지에 유리

- 실행 시간은 Logistic Regression이 5.8초로 빠르지만, 성능은 Random Forest가 더 우수  
  → 속도 우선일 경우 Logistic Regression, 정확한 탐지가 우선이라면 Random Forest 선택

---

## 💡 금융적 시사점

- 사기 탐지는 실시간성과 정확도의 균형이 중요함
- 실무에서는 Random Forest와 같은 앙상블 모델을 활용하되, 속도 보완을 위한 모델 경량화 필요
- 높은 Precision은 고객 불편을 줄이고, 높은 Recall은 실제 사기를 놓치지 않게 도와줌

---

## ✅ 결론

> Random Forest 모델이 신용카드 사기 탐지에 더 효과적이며, 특히 사기를 놓치지 않는 능력(Recall)에서 우수한 성능을 보였다.
