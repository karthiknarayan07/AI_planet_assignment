from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from AI_planet_application.models import Hackathon,Submission
from .serializers import HackathonSerializer,SubmissionSerializer

from AI_planet_application.forms import HackathonForm

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def availableHackathons(request,filterParam):
    if request.method == "GET":

        if filterParam == "available":
            user_submissions = Submission.objects.filter(submitted_by=request.user)
            hackathons_with_submission = Hackathon.objects.filter(submission__in=user_submissions)
            hackathons = Hackathon.objects.exclude(hackathon_id__in=hackathons_with_submission)
            hackathonsData = HackathonSerializer(hackathons,many=True)
            return Response(hackathonsData.data)
        
        if filterParam == "enrolled":
            user_submissions = Submission.objects.filter(submitted_by=request.user,is_submitted=False)
            hackathons_with_submission = Hackathon.objects.filter(submission__in=user_submissions)
            hackathonsData = HackathonSerializer(hackathons_with_submission,many=True)
            return Response(hackathonsData.data)
        
        if filterParam == "submitted":
            user_submissions = Submission.objects.filter(submitted_by=request.user,is_submitted=True)
            hackathons_with_submission = Hackathon.objects.filter(submission__in=user_submissions)
            hackathonsData = HackathonSerializer(hackathons_with_submission,many=True)
            return Response(hackathonsData.data)
        
        if filterParam == "my_hackathons":
            hackathons = Hackathon.objects.filter(created_by=request.user)
            hackathonsData = HackathonSerializer(hackathons,many=True)
            return Response(hackathonsData.data)
        
        return Response({"status":"unknow error"})
    
    if request.method == "POST":

        if filterParam == "create":
            data=request.POST
            hackathon = Hackathon(created_by = request.user,title=data['title'],description=data['description'],submission_type=data['submission_type'],start_datetime=data['start_datetime'],end_datetime=data['end_datetime'],reward_prize=data['reward_prize'])
            hackathon.background_image = request.FILES['background_image']
            hackathon.hackathon_image = request.FILES['hackathon_image']
            hackathon.save()

            return Response({"status":"created new hackathon"})
        return Response({"status":"unknown post error"})



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def viewApplyHackathons(request,action_name,hackathon_id):
    
    if request.method == "GET":
        
        if action_name == "view":
            item = Hackathon.objects.get(hackathon_id=hackathon_id)
            hackathon = HackathonSerializer(item)
            return Response(hackathon.data)
        
        if action_name == "submissions":

            myHackathon = Hackathon.objects.get(hackathon_id=hackathon_id,created_by=request.user)
            myHackathonSubmissions = Submission.objects.filter(hackathon=myHackathon,is_submitted=True)
            submissionsData = SubmissionSerializer(myHackathonSubmissions,many=True)
            return Response(submissionsData.data)
        
        return Response({"status":"unknown error"})
    
    if request.method == "POST":
        if action_name == "enroll":
            hackathon = Hackathon.objects.get(hackathon_id=hackathon_id)
            isAlreadyEnrolled = Submission.objects.filter(hackathon=hackathon,submitted_by=request.user).first()
            if isAlreadyEnrolled == None:
                submission = Submission.objects.create(submitted_by=request.user,hackathon=hackathon,submission_type=hackathon.submission_type)
                submission.save()
                return Response({"status":"enroll succes"})
            return Response({"status":"user already enrolled or submitted"})
        
        if action_name == "submit":
            hackathon = Hackathon.objects.get(hackathon_id=hackathon_id)
            submission = Submission.objects.get(submitted_by=request.user,hackathon=hackathon)
            submission.submission_title = request.POST['submissionTitle']
            submission.summary = request.POST['submissionSummary']
            submission.is_submitted = True

            if request.POST["typeOfSubmission"] == "file":
                file = request.FILES.get('file')
                submission.file.save(file.name,file,save=True)

            if request.POST["typeOfSubmission"] == "image":
                file = request.FILES.get('image')
                submission.image.save(file.name,file,save=True)

            if request.POST["typeOfSubmission"] == "link":
                submission.link = request.POST['link']

            submission.save()

            return Response({'status':'submitted successfully'})
        
    return Response({"status":"unknown error"})

