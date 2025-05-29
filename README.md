This repo was forked from https://github.com/christie-nhs-data-science/DQMaRC and will form the basis of the data profiling tool for the STARTER-KIT project.

# CRUK Data Quality Profiling Tool

A data quality profiling tool built using Python and [Shiny for Python](https://shiny.posit.co/py/), designed to assess oncology data in up to six data quality dimensions. Completeness, Validity, Uniqueness, Timeliness, Consistency, and Accuracy. 

Users can upload their dataset, configure tests, and view results in an interactive dashboard.

## Installation

Instructions for **Windows 11**, **macOS**, and **Linux**.

### Prerequisites

- **Python 3.10** or later — download from: https://www.python.org/downloads/
- Ensure `python` and `pip` are accessible from your command line or terminal e.g.

```bash
pip --version
python --version
```

---

### 1. Clone the Repository

```bash
git clone https://github.com/UoMResearchIT/Data-Quality-Profiling-Tool.git
cd Data-Quality-Profiling-Tool
```

---

### 2. Create and Activate a Virtual Environment

#### On **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On **macOS/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

Install all required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4. Run the App

Start the Shiny application:

```bash
shiny run --reload app.py
```

Then open your browser and navigate to:

`http://localhost:8000`

---
