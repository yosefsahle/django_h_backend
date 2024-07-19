# views.py
from rest_framework import generics
from .models import LibraryTopCategory, LibraryMiddleCategory, LibrarySubCategory, LibraryData
from .serializer import LibraryTopCategorySerializer, LibraryMiddleCategorySerializer, LibrarySubCategorySerializer, LibraryDataSerializer
from rest_framework.permissions import AllowAny

#TOP CATEGORY VIEWS
class LibraryTopCategoryListView(generics.ListAPIView):
    queryset = LibraryTopCategory.objects.all()
    serializer_class = LibraryTopCategorySerializer
    permission_classes = [AllowAny]
class LibraryTopCategoryListCreateView(generics.ListCreateAPIView):
    queryset = LibraryTopCategory.objects.all()
    serializer_class = LibraryTopCategorySerializer
    permission_classes = [AllowAny]

class LibraryTopCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryTopCategory.objects.all()
    serializer_class = LibraryTopCategorySerializer
    permission_classes = [AllowAny]


#MIDDLE CATEGROY VIEWS

class LibraryMiddleCategoryListView(generics.ListAPIView):
    queryset = LibraryMiddleCategory.objects.all()
    serializer_class = LibraryMiddleCategorySerializer
    permission_classes = [AllowAny]
class LibraryMiddleCategoryListCreateView(generics.ListCreateAPIView):
    queryset = LibraryMiddleCategory.objects.all()
    serializer_class = LibraryMiddleCategorySerializer
    permission_classes = [AllowAny]

class LibraryMiddleCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryMiddleCategory.objects.all()
    serializer_class = LibraryMiddleCategorySerializer
    permission_classes = [AllowAny]

class LibraryMiddleCategoryByTopCategoryView(generics.ListAPIView):
    serializer_class = LibraryMiddleCategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        top_category_id = self.kwargs['top_category_id']
        return LibraryMiddleCategory.objects.filter(top_category_id=top_category_id)



#SUB CATEGORY VIEWS

class LibrarySubCategoryListView(generics.ListAPIView):
    queryset = LibrarySubCategory.objects.all()
    serializer_class = LibrarySubCategorySerializer
    permission_classes = [AllowAny]
class LibrarySubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = LibrarySubCategory.objects.all()
    serializer_class = LibrarySubCategorySerializer
    permission_classes = [AllowAny]

class LibrarySubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibrarySubCategory.objects.all()
    serializer_class = LibrarySubCategorySerializer
    permission_classes = [AllowAny]

class LibrarySubCategoryByMiddleCategoryView(generics.ListAPIView):
    serializer_class = LibrarySubCategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        middle_category_id = self.kwargs['middle_category_id']
        return LibrarySubCategory.objects.filter(middle_category_id=middle_category_id)


#LIBRARY DATA VIEWS
class LibraryDataBySubCategoryListView(generics.ListAPIView):
    serializer_class = LibraryDataSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        sub_category_id = self.kwargs['sub_category_id']
        return LibraryData.objects.filter(sub_category_id=sub_category_id)
class LibraryDataListCreateView(generics.ListCreateAPIView):
    queryset = LibraryData.objects.all()
    serializer_class = LibraryDataSerializer
    permission_classes = [AllowAny]

class LibraryDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryData.objects.all()
    serializer_class = LibraryDataSerializer
    permission_classes = [AllowAny]
