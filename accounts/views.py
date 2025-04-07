import csv
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from io import StringIO
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

# Create your views here.
class Inputcsv(APIView):
    parser_classes = (MultiPartParser,FormParser)

    def post(self,request):
        file = request.FILES.get('file')
        if file.content_type != 'text/csv':
            return Response({"error": "invalid file type"}, status=status.HTTP_400_BAD_REQUEST)

        file_view = file.read().decode('utf-8')
        csv_file = StringIO(file_view)
        reader = csv.DictReader(csv_file)
        print(reader)
        saved_records = []
        skipped_records = []
        errors = []

        for row in reader:
            email = row.get("email")
            age = row.get("age")
            try:
                age = int(age)
            except (ValueError, TypeError):
                skipped_records.append({"row": row, "reason": "invalid age format"})
                continue
            if User.objects.filter(email=email).exists() or not (0 <= age <= 120):
                skipped_records.append({"row": row, "reason": "invalid age or email"})
                continue

            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                serializer.save()
                saved_records.append(serializer.data)
            else:
                errors.append({"row": row, "errors": serializer.errors})

        return Response({
            "saved": saved_records,
            "skipped":skipped_records,
            "errors":errors
        })



