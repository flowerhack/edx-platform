from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group

from joinus.models import JoinUs

from courseware.courses import get_course_by_id
from edxmako.shortcuts import render_to_response

def groups(request, course_id):
    """Display the join/create/view groups view."""

    course = get_course_by_id(course_id, depth=None)

    if request.POST:
        g = JoinUs.join_joinus_group(request.user, request.POST['group_name'])
        context = {
            'course': course,
            'group_name': request.POST['group_name'],
        }
    else:
        context = {
            'course': course,
        }
    context['groups']= request.user.groups.filter(name__startswith='joinus')

    return render_to_response('joinus/groups.html', context)

def group_detail(request, group_id, course_id):
    """Display a group."""
    
    course = get_course_by_id(course_id, depth=None)

    context = {
        'course': course,
        'group': Group.objects.get(pk=group_id),
    }
    
    return render_to_response('joinus/group_detail.html', context)

def group_create(request, group_id, course_id):
    """Create a group."""

    course = get_course_by_id(course_id, depth=None)
    #group = JoinUs.

    context = {
        'course': course,
        'group': group,
    }
    
    return render_to_response('joinus/group_detail.html', context)