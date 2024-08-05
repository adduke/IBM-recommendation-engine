# IBM-recommendation-engine


Project contains all files to recommend IBM Watson Studio content.


<p align="center">
  <a href=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwZunj7lvXdtPdRjYbmU-uIzhmFyJD1n23TQ&s>
    <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3AIBM_logo.svg&psig=AOvVaw3U-mcDz7D9liheNIB9KCKo&ust=1722971151414000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMjJk-3F3ocDFQAAAAAdAAAAABAE" alt="#IBM logo" width="200" height="165">
  </a>
</p>

<h3 align="center"># IBM recommendation engine</h3>

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Instructions](#instructions)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

All packages required are in the requirements.txt. To get started with the IBM Recommendation Engine, clone this repository and install the necessary dependencies. Ensure you have Python 3.7 or later installed.

```bash
git clone https://github.com/adduke/IBM-recommendation-engine.git
cd IBM-recommendation-engine
pip install -r requirements.txt ```




## Project Motivation<a name="motivation"></a>

### The Challenge

In the vast world of IBM Watson Studio, users are surrounded by a wealth of articles, datasets, notebooks, and other A.I. and ML assets. With so much content available, it can be overwhelming to find exactly what you need. The challenge here is to sift through this sea of information and present users with the most relevant and useful resources tailored to their interests and needs.

### What We’re Trying to Do

Our goal with this recommendation engine is to make it easier for users to discover and interact with the assets most suited to them. By using smart algorithms to analyze user behavior and preferences, we aim to deliver personalized recommendations that improve the overall experience. Whether it's finding the right dataset for a project or discovering insightful articles, our system is designed to connect users with content that's truly valuable to them.

### Why It Matters

Personalization in the IBM Watson Studio ecosystem isn’t just a nice-to-have; it’s essential for enhancing user engagement and satisfaction. When users receive recommendations that are relevant and tailored to their interests, they’re more likely to find useful content and stay engaged with the platform. This not only improves the individual user experience but also helps users make the most out of the extensive resources available. In a world full of information, making those connections more intuitive and meaningful is what drives a better, more effective experience for everyone.




## File Descriptions <a name="files"></a>

The main script available here to validate the implementation of our work is project_tests.py. Markdown cells were used to assist in walking through the thought process for individual steps.  

README.md: This file, providing an overview of the project.
requirements.txt: Contains a list of Python packages required to run the project.
recommendation_engine.py: The main script that implements the recommendation algorithms.
data/: Directory containing datasets used for training and evaluation.
notebooks/: Jupyter notebooks used for exploratory data analysis and model evaluation.
models/: Directory containing pre-trained models and model configuration files.
scripts/: Helper scripts for data preprocessing, training, and evaluation.


The notebooks folder was used for all necessary development of our model.
```
IBM-recommendation-engine/
│
├── README.md
├── data/
│   ├── articles_community.csv
│   ├── user-item-interactions.csv
│   └── (processed data files like pickles)
│
├── notebooks/
│   ├── EDA.ipynb                      # Exploratory Data Analysis
│   ├── Recommendations_with_IBM.ipynb # Rank Based and User-User Recommendations
│   ├── Recommendations_with_IBM-zh.ipynb # Content Based Recommendations (Optional)
│   └── Recommendation_Model.ipynb     # Matrix Factorization
│
├── src/
│   ├── data_preprocessing.py
│   ├── rank_based_recommendations.py  # Code for Rank Based Recommendations
│   ├── user_user_collaborative_filtering.py # Code for User-User Collaborative Filtering
│   ├── content_based_recommendations.py # Code for Content Based Recommendations (Optional)
│   ├── matrix_factorization.py         # Code for Matrix Factorization
│   ├── project_tests.py
│   └── utils.py
│
├── models/
│   ├── top_10.p
│   ├── top_20.p
│   ├── top_5.p
│   └── user_item_matrix.p
│
└── .ipynb_checkpoints/
    └── (Jupyter notebook checkpoints)


```


## Instructions: <a name="instructions"></a>
1. Run the following commands in the project's root directory to set up your database and model.

    - To apply matrix factorization and generate recommendations
        `python src/matrix_factorization.py`
    - To test the functionality and validate the implementation.
        `python src/project_tests.py`
        ```



## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to IBM.com for the data.  You can find the Licensing for the data and other descriptive information at link available [here](https://www.IBM.com/).  Otherwise, feel free to use the code here as you would like! 
