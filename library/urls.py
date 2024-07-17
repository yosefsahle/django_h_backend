# urls.py
from django.urls import path
from .views import (
    LibraryTopCategoryListCreateView,
    LibraryTopCategoryDetailView,
    LibraryMiddleCategoryListCreateView,
    LibraryMiddleCategoryDetailView,
    LibrarySubCategoryListCreateView,
    LibrarySubCategoryDetailView,
    LibraryDataListCreateView,
    LibraryDataDetailView,
    LibraryTopCategoryListView,
    LibraryMiddleCategoryListView,
    LibrarySubCategoryListView,
    LibraryDataBySubCategoryListView
)

urlpatterns = [
    # Top Category URLs
    path('top-categories/', LibraryTopCategoryListCreateView.as_view(), name='top-category-list-create'),
    path('top-categories/<int:pk>/', LibraryTopCategoryDetailView.as_view(), name='top-category-detail'),
    path('top-categories/all/', LibraryTopCategoryListView.as_view(), name='top-category-list'),

    # Middle Category URLs
    path('middle-categories/', LibraryMiddleCategoryListCreateView.as_view(), name='middle-category-list-create'),
    path('middle-categories/<int:pk>/', LibraryMiddleCategoryDetailView.as_view(), name='middle-category-detail'),
    path('middle-categories/all/', LibraryMiddleCategoryListView.as_view(), name='middle-category-list'),

    # Sub Category URLs
    path('sub-categories/', LibrarySubCategoryListCreateView.as_view(), name='sub-category-list-create'),
    path('sub-categories/<int:pk>/', LibrarySubCategoryDetailView.as_view(), name='sub-category-detail'),
    path('sub-categories/all/', LibrarySubCategoryListView.as_view(), name='sub-category-list'),

    # Library Data URLs
    path('library-data/', LibraryDataListCreateView.as_view(), name='library-data-list-create'),
    path('library-data/<int:pk>/', LibraryDataDetailView.as_view(), name='library-data-detail'),
    path('library-data/by-sub-category/<int:sub_category_id>/', LibraryDataBySubCategoryListView.as_view(), name='library-data-by-sub-category'),
]
