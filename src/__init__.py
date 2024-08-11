# src/__init__.py

"""
This package includes modules for different recommendation algorithms and data processing.
Modules:
- data_preprocessing: Data cleaning and preprocessing functions.
- rank_based_recommendations: Rank-based recommendation algorithms.
- user_user_collaborative_filtering: User-user collaborative filtering algorithms.
- content_based_recommendations: Content-based recommendation algorithms.
- matrix_factorization: Matrix factorization algorithms.
"""

from . import project_tests
# from .data_preprocessing import preprocess_data
# from .rank_based_recommendations import rank_based_function
# from .user_user_collaborative_filtering import user_user_function
# from .content_based_recommendations import content_based_function
# from .matrix_factorization import matrix_factorization_function

__all__ = [
     'project_tests'
#     'preprocess_data',
#     'rank_based_function',
#     'user_user_function',
#     'content_based_function',
#     'matrix_factorization_function'
]

__version__ = '1.0.0'
__author__ = 'Medinat Ibrahim'

