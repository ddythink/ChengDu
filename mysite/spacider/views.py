from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Project
from .models import Report
from .forms import ReportForm

# Create your views here.

def index(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'spacider/index.html', context)


def returnReport(request, pk):
    if request.method == 'GET':
        r = get_object_or_404(Report, pk=pk)
        form = ReportForm(instance=r)

        return render(request, 'spacider/compareReport.html', {'form':form})
    else:
        print "POST"


def report(request, pk):
    try:
        aReport = Report.objects.get(pids=str(pk))
        rid = aReport.id
    except Report.DoesNotExist:
        p = get_object_or_404(Project, pk=pk)
        rname = p.pname
        if p.project_type == 0:
            control = "11111111"
            report_type = 0
        else:
            control = "111111"
            report_type = 1
        r = Report(pids=str(pk), rname=rname, control=control, report_type=report_type)
        r.save()
        rid = r.id
    content = {
        'rid': rid
    }
    return render(request,'spacider/report.html', content)

def compare(request):
    if request.method == 'POST':
        print request.POST.getlist(u'_selected_action') # this code is important getlist() method
    return None

def generate_report(request):
    if request.method == 'POST':
        rawPids = request.POST.getlist(u'_selected_action')
        pids = None
        rid = None
        control = None
        report_type = None
        rname = None
        pidLen = len(rawPids)
        if  pidLen == 0:
            raise Http404
        elif pidLen == 1:
            pids = str(rawPids[0])
        else:
            sorted(rawPids)
            pids = rawPids[0] + '|' + rawPids[1]

        try:
            report = Report.objects.get(pids=pids)
            rid = report.id
        except Report.DoesNotExist:
            if pidLen == 1:
                p = Project.objects.get(pk=int(rawPids[0]))
                rname = p.pname
                if p.project_type == 0:
                    control = "11111111"
                    report_type = 0
                else:
                    control = "111111"
                    report_type = 1
                r = Report(pids=pids, rname=rname, control=control, report_type=report_type)
                r.save()
                rid = r.id
            else:
                pA = Project.objects.get(pk=int(rawPids[0]))
                pB = Project.objects.get(pk=int(rawPids[1]))
                rname = pA.pname + '-' + pB.pname
                control = "1111"
                if pA.locate == pB.locate:
                    report_type = 2
                else:
                    report_type = 3

                r = Report(pids=pids, rname=rname, control=control, report_type=report_type)
                r.save()
                rid = r.id

        content = {
        'rid': rid,
        }

        return  render(request,'spacider/treport.html', content)















