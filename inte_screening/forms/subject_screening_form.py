from django import forms
from edc_form_validators import FormValidatorMixin, FormValidator
from edc_screening.modelform_mixins import AlreadyConsentedFormMixin

from ..form_validators import SubjectScreeningFormValidator
from ..models import SubjectScreening


class SubjectScreeningForm(
    AlreadyConsentedFormMixin, FormValidatorMixin, forms.ModelForm
):

    form_validator_cls = SubjectScreeningFormValidator

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = SubjectScreening
        fields = [
            "screening_consent",
            "selection_method",
            "report_datetime",
            "initials",
            "gender",
            "age_in_years",
            "hospital_identifier",
            "hiv_pos",
            "diabetic",
            "hypertensive",
            "lives_nearby",
            "staying_nearby",
            "requires_acute_care",
            "unsuitable_for_study",
            "reasons_unsuitable",
            "unsuitable_agreed",
        ]
