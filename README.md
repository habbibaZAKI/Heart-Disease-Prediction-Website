# Heart Disease Prediction and Analytics System

A full-stack healthcare application that integrates a Support Vector Machine (SVM) model for risk prediction with a robust data analytics pipeline for population health insights.

## Project Overview

This system allows users to input clinical health data to receive immediate heart disease risk assessments. It concurrently provides a comprehensive analytics dashboard that processes medical records to visualize trends and statistical distributions.

## Core Features

* **Machine Learning Inference**: Implements a pre-trained SVM model to analyze 13 clinical parameters for real-time heart disease classification.
* **Data Aggregation Pipeline**: Extracts raw BSON data from MongoDB Atlas and utilizes the Pandas library for complex statistical transformations.
* **Secure Authentication**: Features a user management system with Bcrypt password hashing and persistent session handling.
* **Automated Data Logging**: Every user prediction is automatically stored in a dedicated collection to build a personal medical history.
* **Dynamic Visualizations**: Generates server-side charts (Histogram, Pie, Bar, and Line plots) using Matplotlib, delivered via Base64 encoding for efficient frontend rendering.

## Technical Stack

* **Backend Framework**: FastAPI (Python)
* **Database**: MongoDB Atlas (NoSQL)
* **Data Analysis**: Pandas and NumPy
* **Machine Learning**: Scikit-learn (SVM Model)
* **Visualization**: Matplotlib
* **Security**: Bcrypt Hashing

## The Analytics Pipeline

The application demonstrates an advanced integration of NoSQL storage and tabular data analysis:

1. **Extraction**: Raw documents are fetched from the MongoDB Dataset collection.
2. **Structuring**: Data is loaded into a Pandas DataFrame for high-speed processing.
3. **Aggregation**: The system calculates population-wide metrics including mean age, median cholesterol, and maximum heart rate.
4. **Grouping**: Utilizes the Split-Apply-Combine pattern to identify correlations, such as average cholesterol levels segmented by age.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**:
   Create a `.env` file in the root directory and add your MongoDB connection string:
   ```
   MONGO_URI=your_mongodb_atlas_connection_string
   ```

4. **Launch the Server**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the Application**:
   Open your browser and navigate to `http://localhost:8000`

## Privacy and Data Lifecycle

The system supports full CRUD operations with a focus on user privacy. The account deletion feature implements a cascading logic that removes a user's profile and all associated medical records from the database permanently.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

* Heart disease dataset providers
* FastAPI and Scikit-learn communities
* MongoDB Atlas for cloud database services
