from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models
from datetime import date, datetime
import random
import string

# ALL IDs MUST BE 8 CHARACTERS LONG
def generate_id():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])

# Making the default Django user's username and email unique
User._meta.get_field('username')._unique = True
User._meta.get_field('email')._unique = True

####################
## GENERAL MODELS ##
####################

# An extension off of the default User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", unique=True) # Extending from default User class
    status = models.CharField(max_length=20, null=True, blank=True) # OPTIONAL: A quick status that the user may update
    biography = models.TextField(max_length=200, null=True, blank=True) # OPTIONAL: A description of the user
    birthday = models.DateField(null=True, blank=True) # OPTIONAL: The birthday of the user
    education = models.CharField(max_length=100, null=True, blank=True) # OPTIONAL: The current/past education of the user
    location = models.CharField(max_length=50, null=True, blank=True) # OPTIONAL: The area around where the user lives
    profile_picture = models.ImageField(null=True, blank=True) # OPTIONAL: A profile picture for the user
    skills = ArrayField(models.CharField(max_length=50), null=True, blank=True) # OPTIONAL: An array of the user's skills

    github_profile = models.CharField(max_length=100, null=True, blank=True) # OPTIONAL: Link to user's GitHub profile
    linkedin_profile = models.CharField(max_length=100, null=True, blank=True) # OPTIONAL: Link to user's LinkedIn profile
    twitter_profile = models.CharField(max_length=100, null=True, blank=True) # OPTIONAL: Link to user's Twitter profile
    instagram_profile = models.CharField(max_length=100, null=True, blank=True) # OPTIONAL: Link to user's Instagram profile
    facebook_profile = models.CharField(max_length=100, null=True, blank=True) # OPTIONAL: Link to user's Facebook profile
    twitch_profile = models.CharField(max_length=100, null=True, blank=True) # OPTIONAL: Link to user's Twitch profile
    personal_website = models.CharField(max_length=100, null=True, blank=True) # OPTIONAL: Link to user's personal website

    past_hackathons = models.ManyToManyField("Hackathon", blank=True) # OPTIONAL: A lit of past w3Hacks hackathons that the user has competed in
    projects = models.ManyToManyField("Project", blank=True) # List of projects created by user
    achievements = models.ManyToManyField("Achievement", blank=True) # List of achievements achieved by the user
    joined_date = models.DateField(default=date.today()) # The date when the user joined w3Hacks
    credits = models.IntegerField(default=0) # The number of credits the user has
    overall_ranking_points = models.IntegerField(default=0) # The overall ranking points the user has
    hackathon_ranking_points = models.IntegerField(default=0) # The hackathon ranking points the user has
    project_ranking_points = models.IntegerField(default=0) # The project ranking points the user has
    quiz_ranking_points = models.IntegerField(default=0) # The quiz ranking points the user has
    exercise_ranking_points = models.IntegerField(default=0) # The exercise ranking points the user has

    def __str__(self):
        return self.user.username


# Project model for each project
class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=8, unique=True, default=generate_id) # Unique ID for project
    title = models.CharField(max_length=50) # Name of the project
    description = models.TextField(max_length=500) # Description of the project
    project_image = models.ImageField(null=True, blank=True) # OPTIONAL: Image of the project
    technologies_used = ArrayField(models.CharField(max_length=30), null=True, blank=True) # OPTIONAL: Array of technologies used for the project
    github_link = models.CharField(max_length=200, null=True, blank=True) # OPTIONAL: Link to the project on GitHub
    project_link = models.CharField(max_length=200, null=True, blank=True) # OPTIONAL: Link to the project if hosted on the app store or Internet
    video_link = models.CharField(max_length=200, null=True, blank=True) # OPTIONAL: Link to a video of project demo
    extra_files = ArrayField(models.FileField(), null=True, blank=True) # OPTIONAL: Array of extra files to submit along with project
    creator = models.ForeignKey("Profile", on_delete=models.PROTECT) # Creator of project
    likes = models.IntegerField(null=True, default=0) # Number of likes on project

    def __str__(self):
        return self.title


# Model for each hackathon, current or not
class Hackathon(models.Model):
    id = models.CharField(primary_key=True, max_length=8, unique=True, default=generate_id) # ID for display
    title = models.CharField(max_length=50) # Name of the hackathon
    description = models.TextField(max_length=300) # Description of the hackathon
    start_datetime = models.DateTimeField() # Starting datetime for the hackathon
    end_datetime = models.DateTimeField() # Ending datetime for the hackathon
    submissions_open_datetime = models.DateTimeField() # Opening datetime for the submissions
    submissions_close_datetime = models.DateTimeField() # Closing datetime for the submissions
    winners_announced = models.DateTimeField() # Datetime to announce winners
    schedule = models.ManyToManyField("ScheduleEvent", blank=True) # List of ScheduleEvents for hackathon
    themes = models.ManyToManyField("Theme", blank=True) # List of themes for hackathon
    awards = models.ManyToManyField("Award", blank=True) # List of awards for hackathon
    resources = models.ManyToManyField("ResourceLink", blank=True) # List of resource links for hackathon
    competitors = models.ManyToManyField("Profile", blank=True) # List of competitor profiles; can be empty in beginning
    submissions = models.ManyToManyField("Project", blank=True) # List of project submissions; can be empty in beginning

    def __str__(self):
        return self.title


####################
## PROFILE MODELS ##
####################

# For user profile achievements
class Achievement(models.Model):
    name = models.CharField(max_length=50) # Name of the achievement
    requirement = models.TextField() # Requirement to achieve the achievement
    credits = models.IntegerField() # Number of credits earned when achieved
    ranking_points = models.IntegerField() # Number of ranking points earned when achieved

    def __str__(self):
        return self.name


# For 'Themes' section of Hackathon
class Theme(models.Model):
    title = models.CharField(max_length=50) # Name of the theme
    description = models.TextField(max_length=300) # Description of the theme

    def __str__(self):
        return self.title


#####################
## EXERCISE MODELS ##
#####################

class Topic(models.Model):
    name = models.CharField(max_length=50) # Name of the topic
    searchable_name = models.CharField(max_length=50) # Name of the topic that will be added into the url extension OR query parameter
    image = models.ImageField() # Image for the topic

    def __str__(self):
        return self.name


class ProjectExercise(models.Model):
    id = models.CharField(primary_key=True, max_length=8, unique=True, default=generate_id) # Unique ID for project exercises
    name = models.CharField(max_length=50) # Name of the project
    description = models.TextField() # Description of the project
    topic = models.ForeignKey("Topic", on_delete=models.PROTECT) # The topic of the exercise 
    difficulty = models.CharField(max_length=10) # The difficulty of the exercise (easy, medium, hard)
    prerequisites = ArrayField(models.CharField(max_length=50)) # List of string prerequisites needed for this project
    resources = models.ManyToManyField("ResourceLink") # Resources for this project

    def __str__(self):
        return self.name


class QuizExercise(models.Model):
    id = models.CharField(primary_key=True, max_length=8, unique=True, default=generate_id) # Unique ID for quiz exercise
    name = models.CharField(max_length=50) # Name of the quiz
    description = models.TextField() # Description of the quiz
    topic = models.CharField(max_length=50) # The topic, programming language, or framework the quiz is based on
    difficulty = models.CharField(max_length=10) # The difficulty of the quiz (easy, medium, hard)
    prerequisites = ArrayField(models.CharField(max_length=50)) # List of string prerequisites needed for this quiz
    resources = models.ManyToManyField("ResourceLink") # Resources for this quiz
    questions = models.ManyToManyField("QuizQuestion") # Questions for this quiz

    def __str__(self):
        return self.name


class MiniExercise(models.Model):
    id = models.CharField(primary_key=True, max_length=8, unique=True, default=generate_id) # Unique ID for mini-exercise
    name = models.CharField(max_length=50) # Name of the mini exercise
    description = models.TextField() # Description of the mini exercise
    topic = models.CharField(max_length=50) # The topic, programming language, or framework the mini exercise  is based on
    difficulty = models.CharField(max_length=10) # The difficulty of the mini exercise  (easy, medium, hard)
    prerequisites = ArrayField(models.CharField(max_length=50)) # List of string prerequisites needed for this mini exercise
    resources = models.ManyToManyField("ResourceLink") # Resources for this mini exercise

    def __str__(self):
        return self.name


# For the QuizExercise model
class QuizQuestion(models.Model):
    question = models.CharField(max_length=100) # The question
    answers = ArrayField(models.CharField(max_length=100)) # Array of possible answers
    correct_answer_index = models.IntegerField() # Index of the correct answer in 'answers' field of this model

    def __str__(self):
        return self.question


# For 'Resources' section of Hackathon
class ResourceLink(models.Model):
    title = models.CharField(max_length=50) # String to be shown on display
    url_extension = models.CharField(max_length=50, unique=True) # String for url extension
    link = models.CharField(max_length=200) # Actual link URL

    def __str__(self):
        return self.title


######################
## HACKATHON MODELS ##
######################

# For each award for Hackathon
class Award(models.Model):
    title = models.CharField(max_length=50) # Name of the award
    description = models.TextField(max_length=300) # Description of the award
    prize = models.CharField(max_length=100) # Prize for the winner of the award
    winner = models.ForeignKey("Profile", on_delete=models.PROTECT, null=True, blank=True) # Winner of the award

    def __str__(self):
        return self.title


# For each event on Hackathon schedule
class ScheduleEvent(models.Model):
    title = models.CharField(max_length=50) # Name of the event
    description = models.TextField(max_length=300) # Description of the event
    event_link = models.ForeignKey("ResourceLink", on_delete=models.CASCADE) # OPTIONAL: Link for the event

    def __str__(self):
        return self.title
