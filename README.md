# Intellectual-Property-Copyright

## Problem
Communication for Effective Debt Recovery
In the world of debt recovery, communication is everything — yet current methods often fall short depending on the client type and situation.

Emails are the preferred mode of communication for corporate clients due to their formality and ease of documentation. However, they often lack urgency and are easily ignored or left unread.

Phone calls add a personal touch and are harder to ignore, making them ideal for follow-ups. Still, many clients avoid answering if they suspect it's related to collections.

Physical visits typically result in stronger repayment commitments and even on-the-spot payments, but they require significant time, cost, and planning. They are also not scalable or practical for clients in remote locations.

## Solution
An Exploration of the Various Message-based Services, Apps, and Web-based Service Solutions

Outcome: Develop a risk management tool - Move away from Excel sheets to a more integrated and transparent visual tool that can provide early predictive analysis of any risks.

## Project Overview
This project is a **Debt Recovery Dashboard** built with Python, Dash, and Plotly. It provides an interactive web-based interface for analyzing debt recovery data, risk assessment, and client management.

### Key Features:
- **Interactive Dashboard**: Real-time data visualization and analysis
- **Risk Assessment**: Automated risk scoring based on multiple factors
- **Client Management**: Detailed client information and payment tracking
- **Data Visualization**: Charts and graphs for better insights
- **Filtering & Sorting**: Advanced data filtering capabilities

## Technology Stack
- **Python 3.12+**
- **Dash** - Web framework for building analytical web applications
- **Plotly** - Interactive plotting library
- **Pandas** - Data manipulation and analysis
- **CSV Data Source** - Debt recovery data stored in CSV format

## Prerequisites
Before testing this project, ensure you have the following installed:

1. **Python 3.12 or higher**
2. **Git** (for cloning the repository)
3. **pip** (Python package installer)

## Step-by-Step Testing Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/Powerlearnproject/Intellectual-Property-Copyright.git
```

### Step 2: Navigate to Project Directory
```bash
cd Intellectual-Property-Copyright
```

### Step 3: Set Up Virtual Environment (Recommended)
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
# Install required packages
pip install dash pandas plotly
```

**Alternative: Create requirements.txt**
If you want to create a requirements file for easier dependency management:
```bash
# Create requirements.txt with the necessary packages
echo "dash>=2.14.0" > requirements.txt
echo "pandas>=2.0.0" >> requirements.txt
echo "plotly>=5.15.0" >> requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

### Step 5: Prepare Data File
The application expects a CSV file named `Debts_Recovery.csv` in the project directory. The CSV should contain the following columns:

**Required CSV Structure:**
```csv
Client Name,Amount Owed (KES),Days Overdue,Risk Level,Last Payment Date,Due Date
Client A,50000,30,High,2024-01-15,2024-02-15
Client B,25000,15,Medium,2024-01-20,2024-02-20
Client C,10000,5,Low,2024-01-25,2024-02-25
```

**CSV Column Descriptions:**
- `Client Name`: Name of the client
- `Amount Owed (KES)`: Amount owed in Kenyan Shillings
- `Days Overdue`: Number of days the payment is overdue
- `Risk Level`: Risk assessment (High/Medium/Low)
- `Last Payment Date`: Date of the last payment (MM/DD/YYYY format)
- `Due Date`: Original due date (MM/DD/YYYY format)

### Step 6: Update File Path (If Necessary)
Open `Debts_Recovery.py` and update the CSV file path if needed:
```python
# Line 7: Update this path to match your CSV file location
df = pd.read_csv("Debts_Recovery.csv")
```

### Step 7: Run the Application
```bash
python Debts_Recovery.py
```

### Step 8: Access the Dashboard
1. Open your web browser
2. Navigate to: `http://127.0.0.1:8050` or `http://localhost:8050`
3. The dashboard should load with interactive visualizations

## Testing Checklist

### ✅ Environment Setup
- [ ] Python 3.12+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed successfully
- [ ] No import errors when running the application

### ✅ Data Preparation
- [ ] CSV file exists in the project directory
- [ ] CSV contains all required columns
- [ ] Data format is correct (dates in MM/DD/YYYY format)
- [ ] File path in code matches actual file location

### ✅ Application Launch
- [ ] Application starts without errors
- [ ] Server runs on localhost:8050
- [ ] Dashboard loads in browser
- [ ] No console errors

### ✅ Dashboard Functionality
- [ ] **KPI Cards**: Total Amount Owed, High Risk Clients, Avg Days Overdue, Recovery Potential
- [ ] **Risk Distribution Chart**: Pie chart showing risk level distribution
- [ ] **Amount by Risk Chart**: Box plot showing amount distribution by risk level
- [ ] **Scatter Plot**: Risk exposure analysis with interactive hover
- [ ] **Payment Trend Chart**: Histogram of payment activity timeline
- [ ] **Client Table**: Sortable and filterable data table
- [ ] **Risk Filter**: Dropdown to filter by risk level

### ✅ Interactive Features
- [ ] Charts are interactive (hover, zoom, pan)
- [ ] Table sorting works (click column headers)
- [ ] Table filtering works (use filter inputs)
- [ ] Risk filter dropdown functions correctly
- [ ] Responsive design works on different screen sizes

### ✅ Data Validation
- [ ] Risk scores are calculated correctly
- [ ] Date calculations are accurate
- [ ] Amount formatting displays properly
- [ ] Risk levels are color-coded appropriately

## Troubleshooting

### Common Issues and Solutions

#### 1. Import Errors
**Problem**: `ModuleNotFoundError: No module named 'dash'`
**Solution**: 
```bash
pip install dash pandas plotly
```

#### 2. File Not Found Error
**Problem**: `FileNotFoundError: [Errno 2] No such file or directory: 'Debts_Recovery.csv'`
**Solution**: 
- Ensure the CSV file exists in the project directory
- Update the file path in `Debts_Recovery.py` line 7

#### 3. Date Format Errors
**Problem**: `ValueError: time data '2024-01-15' does not match format '%m/%d/%Y'`
**Solution**: 
- Ensure dates in CSV are in MM/DD/YYYY format
- Example: `01/15/2024` not `2024-01-15`

#### 4. Port Already in Use
**Problem**: `OSError: [Errno 48] Address already in use`
**Solution**: 
- Change the port in the code: `app.run_server(debug=True, port=8051)`
- Or kill the process using the port

#### 5. Browser Not Loading
**Problem**: Dashboard doesn't load in browser
**Solution**: 
- Check if the server is running (look for "Dash is running on http://127.0.0.1:8050")
- Try different browsers
- Check firewall settings

## Performance Testing

### Load Testing
1. **Small Dataset** (< 100 records): Should load instantly
2. **Medium Dataset** (100-1000 records): Should load within 5 seconds
3. **Large Dataset** (> 1000 records): May take 10-15 seconds

### Browser Compatibility
- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge

## Security Considerations
- The application runs locally and doesn't expose data externally
- No sensitive data should be included in the CSV file
- Consider using environment variables for any API keys in production

## Future Enhancements
- Add user authentication
- Implement data export functionality
- Add more advanced analytics
- Create mobile-responsive design
- Add real-time data updates

## Support
If you encounter issues during testing:
1. Check the console for error messages
2. Verify all prerequisites are installed
3. Ensure data format is correct
4. Try restarting the application

## Happy Testing! 🚀
