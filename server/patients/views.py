from django.http import Http404
from django.views.generic.base import TemplateView

from .models import Patient
from .models import PatientProperty
from .models import PatientStory
from .models import PatientStoryExcerpt

class PatientStoryList(TemplateView):

    template_name = "patient-story-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        patients = Patient.objects.order_by('name') \
        .filter(published = True) \
        .all()

        patient_properties = PatientProperty.objects.filter(
            patient_id__in = [patient.id for patient in patients]
        ) \
        .order_by('order') \
        .prefetch_related('property') \
        .all()

        properties_by_patient_id = {}
        for patient_property in patient_properties:
            patient_id = patient_property.patient_id
            if patient_id not in properties_by_patient_id:
                properties_by_patient_id[patient_id] = []
            properties_by_patient_id[patient_id].append({
                'name': patient_property.property.name,
                'value': patient_property.value
            })

        story_excerpts = PatientStoryExcerpt.objects.filter(
            patient_id__in = [_p.id for _p in patients]
        ) \
        .order_by('order') \
        .all()

        story_excerpts_by_patient_id = {}
        for _excerpt in story_excerpts:
            if _excerpt.patient_id not in story_excerpts_by_patient_id:
                story_excerpts_by_patient_id[_excerpt.patient_id] = []
            story_excerpts_by_patient_id[_excerpt.patient_id].append(
                _excerpt.content
            )

        serialized_patients = []
        for patient in patients:
            properties = []
            if patient.id in properties_by_patient_id:
                properties = properties_by_patient_id[patient.id]
            story_excerpts = []
            if patient.id in story_excerpts_by_patient_id:
                story_excerpts = story_excerpts_by_patient_id[patient.id]
            serialized_patients.append({
                'id': patient.id,
                'name': patient.name,
                'properties': properties,
                'story_excerpts': story_excerpts
            })
        context['patients'] = serialized_patients
        return context

class PatientStoryView(TemplateView):

    template_name = 'patient-story.html'

    def get_patient(self, patient_id):
        try:
            return Patient.objects.get(id = patient_id)
        except Patient.DoesNotExist:
            raise Http404('Patient does not exist')
    
    def get_context_data(self, patient_id, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = self.get_patient(patient_id)
        context['patient'] = {
            'id': patient.id,
            'name': patient.name
        }
        stories = []
        story_query = PatientStory.objects.filter(patient = patient)
        for story in story_query.all():
            stories.append({
                'id': story.id,
                'title': story.title,
                'content': story.content
            })
        context['stories'] = stories
        return context
