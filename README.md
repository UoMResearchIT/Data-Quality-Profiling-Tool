# CRUK Data Quality Profiling Tool

A data quality profiling tool built using Python and [Shiny for Python](https://shiny.posit.co/py/), designed to assess oncology data in up to six data quality dimensions. Completeness, Validity, Uniqueness, Timeliness, Consistency, and Accuracy. 

Users can upload their dataset, configure tests, and view results in an interactive dashboard.

Forked from https://github.com/christie-nhs-data-science/DQMaRC

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

## Usage

1. Upload your data (as a ZIP of multiple CDM files, or as a flat CSV or Excel file) in the Data Upload tab.
   
2. Initialise, edit, and/or upload thresholds and test parameter 'rule sheets' in the Test Parameters tab.
   
3. Run your checks in the Dashboard tab.
   
4. Test results will be displayed in an interactive dashboard in the Dashboard tab.

5. Download results from the Dashboard tab if required.
