# CS50's FINALE PROJECT (Introduction to Computer Science)

## Name: NutriCalcul - Nutrition calculator (HealthCalcul)

**Programming Language Used: Python, HTML, JavaScript, CSS**

---

## Overview
**NutriCalcul** is a web application built with **Python**, **HTML**, **JavaScript**, and **CSS** that helps users:
- Calculate **Body Mass Index** (BMI / Quetelet's index)
- Determine **Ideal Weight** (Robinson's formula)
- Estimate **Daily Energy Requirements** (Black's formula)
- Track the evolution of these metrics over time
- Learn about **nutritional health** through educational resources

---
## A few screenshots
<div style="display: flex; flex-direction: row;">
  <img src="/images/Final/Screenshot%201.png" alt="image1" width="20%" height="20%"> 
  <img src="/images/Final/Screenshot%202.png" alt="image2" width="20%" height="20%">
  <img src="/images/Final/Screenshot%203%20(2).png" alt="image3" width="20%" height="20%">
</div>
<div style="display: flex; flex-direction: row;">
  <img src="/images/Final/Screenshot%204.png" alt="image4" width="20%" height="20%">
  <img src="/images/Final/Screenshot%205.png" alt="image5" width="20%" height="20%">
  <img src="/images/Final/Screenshot%206.png" alt="image6" width="20%" height="20%">
</div>
<div style="display: flex; flex-direction: row;">
  <img src="/images/Final/Screenshot%207.png" alt="image7" width="20%" height="20%">
  <img src="/images/Final/Screenshot%208.png" alt="image8" width="20%" height="20%">
</div>
---


## **Features**

### 1. **User Registration & Authentication**
- Register with:
  - Unique username
  - Password (minimum 4 characters)
  - Sex (Male / Female)
- Secure login/logout system.

### 2. **Data Entry**
- After login, user inputs:
  - **Age** (> 18 years)
  - **Height** (m)
  - **Weight** (kg)
- Submit button remains disabled until all three fields are filled.

### 3. **Main Pages**
- **BMI Page**
  - Displays **latest** BMI in kg/m²
  - Shows **interpretation** of the BMI value
  - Includes an **educational healthy eating pyramid**
  
- **Ideal Weight Page**
  - Displays **latest** ideal weight (kg) using **Robinson's formula**
  - Includes a **food pyramid** with proportions for balanced nutrition
  
- **Energy Requirements Page**
  - Displays **latest** daily energy needs (kcal/24h) via **Black's formula**
  - Shows a **healthy eating plate** with nutritional information
  
- **History Page**
  - Visualizes trends over time for:
    - Height
    - Weight
    - BMI
    - Ideal Weight
    - Energy Requirements
  - Enables tracking of progress and health changes

### 4. **Educational Content**
- Integrated health graphics and explanations to improve nutritional knowledge.

---

## **Why It’s Useful**
The **History** feature makes the application valuable by allowing users to:
- Maintain personalized accounts
- Store and retrieve health metrics over time
- Access past data anytime for progress tracking

---

## **Technical Stack**
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQL (SQLite)
- **Authentication**: Session-based login

---

## **Usage Instructions**
1. **Register** with your credentials.
2. **Login** to your account.
3. Enter your **age**, **height**, and **weight**.
4. Navigate through:
   - **BMI**
   - **Ideal Weight**
   - **Energy Requirements**
   - **History**
5. Review your results and educational content.
6. **Logout** when finished.

---

# Appreciation for the CS50 Experience

I enjoy the training and would like to express my sincere appreciation to the cs50' team.

Sincerely yours.

---