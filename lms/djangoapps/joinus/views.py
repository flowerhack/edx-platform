from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from joinus.models import JoinUs

from courseware.courses import get_course_by_id
from edxmako.shortcuts import render_to_response


@login_required
def groups(request, course_id):
    """Display the join/create/view groups view."""

    course = get_course_by_id(course_id, depth=None)

    context = {
        'course': course,
        'groups': JoinUs.objects.filter(user=request.user),
        'leader_of': JoinUs.objects.filter(leaders=request.user),
    }
    if request.POST:
        if request.POST.get('group_name'): # User wants to join an existing group
            g = JoinUs.join_joinus_group(request.user, request.POST['group_name'])
            context['group_name'] = request.POST['group_name']
        elif request.POST.get('new_group'): # User wants to create a new group
            g = JoinUs.create_joinus_group(user=request.user, gname=request.POST['new_group'])
            context['group'] = g
    else: # Just display the regular page
        pass

    return render_to_response('joinus/groups.html', context)


@login_required
def group_detail(request, group_name, course_id):
    """Display a group."""

    course = get_course_by_id(course_id, depth=None)

    context = {
        'course': course,
        'group': JoinUs.group(group_name),
    }

    return render_to_response('joinus/group_detail.html', context)