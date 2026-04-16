# Affinsys Assignment — UI Test Automation

This project contains a UI automation test built using **Playwright (Python)** and **Pytest**, following the **Page Object Model (POM)** design pattern.

---

##  Tech Stack

* **Python 3**
* **Pytest**
* **Playwright (Sync API)**
* **Page Object Model (POM)**

---

##  Project Structure

```
Affinsys-Assignment/
│
├── pages/                     # Page Object classes
│   ├── home_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── ui_tests/                  # Test cases
│   └── test_add_to_cart.py
```

---

##  Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv .venv
```

### 2. Activate Environment

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pytest playwright
```

### 4. Install Browser

```bash
python -m playwright install chromium
```

---

##  Run Test

```bash
pytest ui_tests/test_add_to_cart.py -s
```

 The test runs in **headful mode** (browser visible).
To run in headless mode, update:

```python
p.chromium.launch(headless=True)
```

---

##  Test Scenario

The test automates the following flow:

1. Open the website
2. Select a product
3. Add product to cart (twice)
4. Refresh the page
5. Open cart
6. Verify:

   * Product is present
   * Total price is correct
   * Quantity is correct
   * Checkout button is visible
7. Proceed to checkout

---

##  Assumptions

* Target website is accessible
* UI locators remain stable
* Chromium browser works locally

---

##  Design Decisions

* **Page Object Model (POM):**
  Separates test logic from UI interactions for better maintainability

* **Playwright:**
  Used for reliable automation with built-in waiting and modern selectors

* **Pytest:**
  Lightweight framework for easy execution and scalability


---

##  Notes

* Uses Playwright **sync API** for simplicity
* Assertions handled via `expect()` for better readability
* Designed to be simple, scalable, and interview-friendly
