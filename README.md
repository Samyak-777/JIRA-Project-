# Change Calculator - JIRA Project Management Assignment

## 📋 Project Overview

This repository contains a **Change Calculator Python Program** developed as part of **CSP300 - Software Lab III** assignment at **VNIT**. The project demonstrates comprehensive **project management using JIRA** while implementing a coin change algorithm.

### 🎯 Assignment Objective
- **Primary**: Implement a Python program that calculates optimal coin change for amounts less than $1.00
- **Secondary**: Demonstrate professional project management using JIRA software
- **Integration**: Track development workflow, issues, and progress through JIRA-GitHub integration

## 💰 Problem Statement

Given a price in cents (< 100), determine the method of giving change that uses the **fewest coins** possible using:
- **Quarters** (25 cents)
- **Dimes** (10 cents) 
- **Nickels** (5 cents)
- **Pennies** (1 cent)

### Example Output
```
The price of your item is 67 cents, and your change is 33 cents.
Here's the change that uses the fewest coins:
pennies: 3
nickels: 1
dimes: 0
quarters: 1
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Git for version control
- JIRA account (for project tracking)

### Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/JIRA-Project.git
   cd JIRA-Project
   ```

2. **Run the program**
   ```bash
   python find_change.py
   ```

3. **Modify the price** (edit line 28 in `find_change.py`)
   ```python
   price = 67  # Change this value to test different scenarios
   ```

## 📁 Project Structure

```
JIRA-Project/
│
├── find_change.py          # Main program file
├── test_cases.py                 # Unit tests for validation
├── requirements.txt              # Python dependencies (if any)
├── docs/                        
│   ├── jira_workflow.md         # JIRA project management documentation
│   ├── installation_guide.md    # Detailed setup instructions
│   └── evaluation_summary.pdf   # Assignment evaluation summary
├── screenshots/
│   ├── jira_dashboard.png       # JIRA project dashboard
│   ├── sprint_board.png         # Scrum board view
│   └── github_integration.png   # GitHub-JIRA integration
└── README.md                    # This file
```

## 🔧 Algorithm Implementation

The program uses a **greedy algorithm** approach to minimize coin count:

```python
def calculate_change(price):
    change = 100 - price
    
    quarters = change // 25
    remaining_after_quarters = change % 25
    
    dimes = remaining_after_quarters // 10
    remaining_after_dimes = remaining_after_quarters % 10
    
    nickels = remaining_after_dimes // 5
    pennies = remaining_after_dimes % 5
    
    return change, pennies, nickels, dimes, quarters
```

### Mathematical Operations Used
- **Integer Division** (`//`): Calculate maximum coins of each denomination
- **Modulus** (`%`): Calculate remaining amount after each coin type
- **Subtraction** (`-`): Calculate total change from $1.00

## 📊 JIRA Integration & Project Management

### 🎯 Project Tracking
This project is fully managed through JIRA with the following structure:

#### **Epic**: Change Calculator Application Development
- **Story 1**: Implement Change Calculation Algorithm
  - Task: Write basic coin calculation function
  - Task: Implement input validation  
  - Task: Add output formatting
- **Story 2**: Testing and Quality Assurance
  - Task: Create comprehensive test cases
  - Task: Fix edge cases and bugs
  - Task: Performance optimization

#### **Sprint Management**
- **Sprint 1**: Core algorithm implementation
- **Sprint 2**: Testing and bug fixes
- **Sprint 3**: Documentation and integration

### 🔗 GitHub-JIRA Integration Features

1. **Commit Linking**: Commits reference JIRA issues
   ```bash
   git commit -m "CCP-1: Implemented basic change calculation algorithm"
   git commit -m "CCP-3: Fixed edge case for zero cents input"
   ```
2. **Automated Issue Updates**: GitHub commits automatically update JIRA issue status
3. **Development Panel**: JIRA shows linked commits, branches, and pull requests
4. **Traceability**: Full development history tracked from requirement to deployment

## 🧪 Test Cases

| Input Price | Expected Change | Quarters | Dimes | Nickels | Pennies | Status |
|-------------|-----------------|----------|-------|---------|---------|---------|
| 67 cents    | 33 cents       | 1        | 0     | 1       | 3       | ✅ Pass |
| 99 cents    | 1 cent         | 0        | 0     | 0       | 1       | ✅ Pass |
| 25 cents    | 75 cents       | 3        | 0     | 0       | 0       | ✅ Pass |
| 1 cent      | 99 cents       | 3        | 2     | 0       | 4       | ✅ Pass |

## 📈 JIRA Reports & Analytics

### Available Reports
- **Sprint Burndown Chart**: Work completion progress
- **Velocity Chart**: Team performance metrics  
- **Cumulative Flow Diagram**: Work in progress analysis
- **Issue Statistics**: Bug resolution and task completion rates

### Automation Rules Implemented
1. **Auto-assignment**: New issues automatically assigned based on workload
2. **Status Updates**: Commits automatically move issues to "In Progress"
3. **Notification Rules**: Team notifications for critical bugs

## 🛠️ Technologies Used

- **Programming Language**: Python 3.7+
- **Project Management**: JIRA Software (Cloud)
- **Version Control**: Git & GitHub
- **Integration Tools**: GitHub for JIRA app
- **Development Methodology**: Agile/Scrum

## 👥 Team Configuration

| Role | Responsibility | JIRA Assignment |
|------|----------------|-----------------|
| Project Lead | Overall coordination | Auto-assigned critical issues |
| Developer | Code implementation | Programming tasks |
| Tester | Quality assurance | Bug verification and testing |

### Assignment Rubrics Coverage

- ✅ **Rubric 1** (4 marks): JIRA installation and project creation
- ✅ **Rubric 2** (4 marks): Plugin configuration and setup
- ✅ **Rubric 3** (6 marks): Executable Python program with JIRA tracking
- ✅ **Rubric 4** (6 marks): GitHub integration and external tool connectivity

## 📝 Usage Examples

### Basic Execution
```bash
$ python find_change.py
The price of your item is 67 cents, and your change is 33 cents.
Here's the change that uses the fewest coins:
pennies: 3
nickels: 1
dimes: 0
quarters: 1
```

### Testing Different Values
Modify the `price` variable in the code to test various scenarios:
- `price = 1` → Maximum change (99 cents)
- `price = 99` → Minimum change (1 cent)  
- `price = 50` → Mid-range testing (50 cents change)

## 🐛 Known Issues & Resolutions

Issues tracked and resolved through JIRA:

1. **CCP-5**: Initial algorithm didn't handle 0 cent input → **Resolved**
2. **CCP-7**: Output formatting inconsistency → **Resolved**
3. **CCP-9**: Missing input validation → **In Progress**

## 🤝 Contributing

This is an academic assignment project. For evaluation purposes:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes with JIRA issue reference (`git commit -m 'CCP-X: Description'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request linked to JIRA issue

## 📄 Documentation

- [JIRA Workflow Guide](docs/jira_workflow.md)
- [Installation Instructions](docs/installation_guide.md)
- [Evaluation Summary](docs/evaluation_summary.pdf)

## 🏆 Evaluation Deliverables

For successful assignment completion, this repository demonstrates:

1. ✅ **Working Python Program**: Fully functional change calculator
2. ✅ **JIRA Project Management**: Complete project lifecycle tracking  
3. ✅ **Integration Showcase**: GitHub-JIRA seamless connectivity
4. ✅ **Professional Workflow**: Industry-standard development practices
5. ✅ **Comprehensive Documentation**: Academic and technical requirements 

**Note**: This project is developed for academic evaluation at VNIT Nagpur and demonstrates practical application of software project management principles using JIRA in conjunction with Python programming.
