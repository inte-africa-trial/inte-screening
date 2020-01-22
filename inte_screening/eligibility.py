from django.utils.safestring import mark_safe
from edc_constants.constants import FEMALE, MALE, YES, TBD, NO
from edc_utils.date import get_utcnow


class SubjectScreeningEligibilityError(Exception):
    pass


class EligibilityPartOneError(Exception):
    pass


class EligibilityPartTwoError(Exception):
    pass


class EligibilityPartThreeError(Exception):
    pass


def check_eligible_final(obj):
    """Updates model instance fields `eligible` and `reasons_ineligible`.
    """
    reasons_ineligible = []

    if obj.unsuitable_for_study == YES:
        obj.eligible = False
        reasons_ineligible.append("Subject unsuitable")
    else:
        obj.eligible = (
            obj.hiv_pos == YES or obj.diabetic == YES or obj.hypertensive == YES)

    if obj.eligible:
        obj.reasons_ineligible = None
    else:
        if obj.hiv_pos == YES:
            reasons_ineligible.append("HIV(+)")
        if obj.diabetic == YES:
            reasons_ineligible.append("Diabetic")
        if obj.hypertensive == YES:
            reasons_ineligible.append("Hypertensive")
        if reasons_ineligible:
            obj.reasons_ineligible = "|".join(reasons_ineligible)
        else:
            obj.reasons_ineligible = None
    obj.eligibility_datetime = get_utcnow()


def format_reasons_ineligible(*str_values):
    reasons = None
    str_values = [x for x in str_values if x is not None]
    if str_values:
        str_values = "".join(str_values)
        reasons = mark_safe(str_values.replace("|", "<BR>"))
    return reasons
