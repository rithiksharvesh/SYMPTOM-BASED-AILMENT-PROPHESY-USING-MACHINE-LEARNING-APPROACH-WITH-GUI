## 🩺 Symptom-Based Ailment Prophesy Using Machine Learning with GUI

A machine learning-based system that predicts diseases based on selected symptoms using a graphical user interface. The project integrates four classification algorithms and achieves up to **95% accuracy**, providing users with instant health insights.

---

## 📌 Project Steps

### 1. **Objective**
- Enable users to predict potential diseases based on symptoms.
- Simplify healthcare access for users who can't immediately consult a doctor.
- Build a user-friendly GUI that utilizes ML models for prediction.

---

### 2. **Dataset Description**
- **Source:** Kaggle – “Disease Prediction Using Machine Learning”
- **Data Details:**
  - Two CSV files: `Training.csv` and `Testing.csv`
  - **132 symptoms** (features) mapped to **26 diseases**

---

### 3. **Data Preprocessing**
- **Integration** – Combined multiple data sources (if any)
- **Transformation** – Converted categorical values
- **Reduction** – Removed redundant features
- **Cleaning** – Handled missing or inconsistent data

---

### 4. **Model Building**
- **Training Data** – Used for building and tuning the ML models
- **Testing Data** – Used for performance validation

- **Algorithms Used:**
  - 🔹 Decision Trees
  - 🔹 Random Forest
  - 🔹 Naive Bayes
  - 🔹 Support Vector Machine (SVM)

Each algorithm was trained to classify one of the 26 diseases based on user-input symptoms.

---

### 5. **Prediction Flow**
1. User selects symptoms via GUI.
2. System maps symptoms to feature vector.
3. ML model(s) predict the most probable disease.
4. Prediction is displayed on the GUI.

---

### 6. **Performance Analysis**
- Achieved an **accuracy of 95%**, significantly better than baseline models (typically ~80%).
- Evaluated using:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **F1-Score**

---

### 7. **Graphical User Interface (GUI)**
- Built to be intuitive and user-friendly.
- Symptom selection through dropdowns or checklists.
- Displays predicted disease with an option for additional recommendations.

---

### 8. **Future Enhancements**
- Integrate recommendations for **doctors** and **hospitals** based on predicted illness.
- Expand the dataset to cover **more diseases** and **multi-label predictions**.
- Deploy as a **web or mobile application**.

---

## 📚 References
- Includes scientific papers and conference articles on disease prediction using machine learning (see full list in the PPT for citation details).

---

