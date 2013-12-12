from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group

from courseware.courses import get_course_by_id
from edxmako.shortcuts import render_to_response

def groups(request, course_id):
    """Display the join/create/view groups view."""

    course = get_course_by_id(course_id, depth=None)

    if request.POST:
        context = {
            'course': course,
            'invitation_code': request.POST['invitation_code'],
        }
    else:
        context = {
            'course': course,
        }

    return render_to_response('joinus/groups.html', context)

def group_detail(request, group_id, course_id):
    """Display a group."""
    
    course = get_course_by_id(course_id, depth=None)

    context = {
        'course': course,
        'group': Group.objects.get(pk=group_id),
    }
    
    return render_to_response('joinus/group_detail.html', context)