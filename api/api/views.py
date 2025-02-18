from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lead
from .serializers import LeadSerializer

# List all leads
@api_view(['GET'])
def get_leads(request):
    leads = Lead.objects.all()
    serializer = LeadSerializer(leads, many=True)
    return Response(serializer.data)

# Create a new lead
@api_view(['POST'])
def create_lead(request):
    serializer = LeadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Get a specific lead by ID
@api_view(['GET'])
def get_lead(request, lead_id):
    try:
        lead = Lead.objects.get(id=lead_id)
    except Lead.DoesNotExist:
        return Response({'error': 'Lead not found'}, status=404)
    serializer = LeadSerializer(lead)
    return Response(serializer.data)

# Update a specific lead
@api_view(['PUT'])
def update_lead(request, lead_id):
    try:
        lead = Lead.objects.get(id=lead_id)
    except Lead.DoesNotExist:
        return Response({'error': 'Lead not found'}, status=404)

    serializer = LeadSerializer(lead, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# Delete a specific lead
@api_view(['DELETE'])
def delete_lead(request, lead_id):
    try:
        lead = Lead.objects.get(id=lead_id)
    except Lead.DoesNotExist:
        return Response({'error': 'Lead not found'}, status=404)
    lead.delete()
    return Response(status=204)
