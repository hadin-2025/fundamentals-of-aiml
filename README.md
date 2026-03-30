# fundamentals-of-aiml

# 📊 Customer Segmentation Using Basic Machine Learning (Without Libraries)

## 📌 Project Overview

This project demonstrates customer segmentation using simple machine learning logic implemented in pure Python, without using any external libraries. Customers are grouped based on their income and spending behavior using dynamically calculated thresholds (averages).

---

## 🎯 Objective

* To understand the basics of customer segmentation
* To implement machine learning logic without libraries
* To classify customers into meaningful groups

---

## 🧠 Method Used

The project uses a **dynamic rule-based approach**:

* Calculates **average income** and **average spending**
* Uses these values as thresholds
* Classifies customers into segments:

  * High Value
  * Wealthy
  * Big Spender
  * Low Value

---

## 🗂️ Dataset

Sample dataset used in the project:

```python
customers = [
    ["Amit", 30000, 40],
    ["Riya", 60000, 80],
    ["John", 25000, 20],
    ["Sara", 58000, 75],
    ["Raj", 90000, 30]
]
```

---

## ⚙️ How It Works

1. Calculate average income and spending
2. Compare each customer’s values with averages
3. Assign a segment based on conditions

---

## ▶️ How to Run

1. Install Python (no extra libraries needed)
2. Copy the code into a `.py` file
3. Run the file using:

```
python filename.py
```

---

## 📈 Sample Output

```
Avg Income: 52600
Avg Spending: 49

Amit -> Low Value
Riya -> High Value
John -> Low Value
Sara -> High Value
Raj -> Wealthy
```

---

## ✅ Advantages

* Simple and easy to understand
* No external dependencies
* Good for beginners

---

## ⚠️ Limitations

* Not suitable for large datasets
* Less accurate than advanced ML algorithms
* Uses basic logic instead of learning complex patterns

---

## 🚀 Future Improvements

* Add more customer features (age, location, frequency)
* Use median instead of average
* Implement advanced ML algorithms
* Visualize results using graphs

---

## 👨‍💻 Conclusion

This project shows how basic machine learning concepts can be applied using simple Python logic. It helps beginners understand how data can be used to make decisions and segment customers effectively.

---
