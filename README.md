# Streamlit App Setup Guide

Follow these steps to set up and run the Streamlit app using virtualenv:

## Step 1: Create a Virtual Environment

```bash
# Create a virtual environment named 'venv'
python -m venv venv
```

## Step 2: Activate the Virtual Environment

### For Windows:

```bash
venv\Scripts\activate
```

### For macOS/Linux:

```bash
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
# Install dependencies from requirements.txt
pip install -r requirements.txt
```

## Step 4: Start Streamlit App

```bash
# Run the Streamlit app (assuming your main file is named 'main.py')
streamlit run main.py
```

Now, your Streamlit app should be running locally. Open a web browser and navigate to the provided URL to interact with your application.

Remember to deactivate the virtual environment when you're done:

```bash
# Deactivate the virtual environment
deactivate
```

Happy coding!
