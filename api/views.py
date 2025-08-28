from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer
from .models import Patient, Doctor, PatientDoctorMapping


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class PatientListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

class DoctorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer

class MappingPatientDetailView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientDoctorMappingSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)

class MappingDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer