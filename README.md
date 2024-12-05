# Automated News Article Summarization Leveraging IBM Natural Language Understanding

## **Project Description**
This project aims to automate the summarization of news articles using **IBM's Natural Language Understanding (NLU)**. By leveraging IBM Watson's advanced NLU services, the application extracts meaningful insights such as entities, keywords, and sentiment to help users quickly grasp essential information from lengthy content. This tool is especially beneficial for users who want a quick summary without reading the entire article.

---

## **Technologies Used**
- **Python**: The core programming language used to implement the application.
- **Flask**: A lightweight Python framework used to build the web application.
- **Requests**: Used to fetch content from external web pages.
- **BeautifulSoup**: For parsing and extracting content from HTML web pages.
- **IBM Watson NLU**: To analyze text and extract meaningful data like entities and keywords.
- **HTML**: For creating the user interface of the web application.

---

## **Project Setup**

### **1. Required Libraries**
The following Python libraries are used in this project:
- `Flask`: For the web application framework.
- `Requests`: To fetch web content from external URLs.
- `BeautifulSoup`: For parsing HTML content.
- `IBM Watson SDK`: For accessing IBM Watson NLU services.

### **2. Setting Up Your Development Environment**

1. **Install Visual Studio Code (VS Code)**
   - Download and install [VS Code](https://code.visualstudio.com/).
  
2. **Install Python**
   - Download and install [Python](https://www.python.org/).
   - Ensure that Python is added to your system's PATH.

### **3. Installation of Required Libraries**

To install the required libraries, run the following command in your terminal:

```bash
pip install flask requests beautifulsoup4 ibm-watson
