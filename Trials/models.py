
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv, os, random
doc = ''


class Constants(BaseConstants):
    name_in_url = 'Judgment_experiment'
    players_per_group = 2

    # find all images and videos
    image_path = os.path.join('_statikk/my_folder/')
    images = os.listdir(image_path)  # this generates a list of filenames
    images = ["my_folder/" + x for x in images] # gives correct relative path to filenames
    images.sort()


    # Find all questions, split into list
    question = open('_statikk/questions_all.txt').read()
    questionsplit = [x for x in question.split('\n')]  # this generates a list of the actual questions as strings

    # Get anchors
    anchorslist = open('_statikk/anchors.txt').read()
    anchors = [x for x in anchorslist.split('\n')]
    
    # Get reference to type of stimuli on stimuli/stimuli-rewatch page 
    stimulilist = open('_statikk/type_stimuli.txt').read()
    stimulitype = [x for x in stimulilist.split('\n')]

    #Get reference to type of stimuli on wavelength page
    image_video = open('_statikk/image_video.txt').read()
    image_video_type = [x for x in image_video.split('\n')]
    
    num_rounds = len(questionsplit) #number of trials equal to number stimuli





class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            number = [x for x in range(len(Constants.questionsplit))]  # list of positions to draw stims from image and question list
            random.shuffle(number) # randomize order
            self.session.vars['stim_order'] = number





class Group(BaseGroup):
    discussion1 = models.FloatField()
    def live_slider(self, id_in_group, package):
        broadcast = {"slider_value": package["slider_value"], "disable": package["disable"]}
        return {0: broadcast}


class Player(BasePlayer):
    Stimulus_displayed = models.StringField()
    Question_displayed = models.StringField()
    PartnerAgreement = models.StringField(choices=[['Strongly disagree', 'Strongly disagree'], ['Disagree', 'Disagree'], ['Somewhat disagree', 'Somewhat disagree'], ['Neither agree nor disagree', 'Neither agree nor disagree'], ['Somewhat agree', 'Somewhat agree'], ['Agree', 'Agree'], ['Strongly agree', 'Strongly agree']], label='', widget=widgets.RadioSelect)
    judgement1 = models.FloatField()
    certainty1 = models.FloatField()
    judgement2 = models.FloatField()
    certainty2 = models.FloatField()
    judgement3 = models.FloatField()
    certainty3 = models.FloatField()
    morality1 = models.FloatField()
    morality2 = models.FloatField()
    mutual_judgment = models.IntegerField()
    my_field = models.StringField()

    PQ_1 = models.StringField()
    PQ_2 = models.StringField()
    PQ_3 = models.StringField()
    PQ_4 = models.StringField()
    PQ_5 = models.StringField()
    PQ_6 = models.StringField()
    PQ_7 = models.LongStringField()
    PQ_8 = models.StringField()
    PQ_9 = models.StringField()
    PQ_10 = models.StringField()
    PQ_11 = models.StringField()
    IOS_1 = models.StringField()

    def my_method(self):
        "live_slider"
    def vars_for_template(self):
        # get image
        stim_name = Constants.images[self.session.vars['stim_order'][self.round_number-1]]

        #check if stim is image or video
        if stim_name.split('.')[1]=="png":
            is_image = 1
        else:
            is_image = 0

        # Get question
        this_question = Constants.questionsplit[self.session.vars['stim_order'][self.round_number-1]]

        # Get anchors
        anchors = Constants.anchors[self.session.vars['stim_order'][self.round_number-1]]
        anchorssplit = [x for x in anchors.split(',')]
        anchor1 = anchorssplit[0]
        anchor2 = anchorssplit[1]

        # Get reference to stimuli time (image/video)
        stimulitype = Constants.stimulitype[self.session.vars['stim_order'][self.round_number-1]]
        
        # Get reference to stimuli on wavelength page
        image_video_type = Constants.image_video_type[self.session.vars['stim_order'][self.round_number-1]]

        return dict(stim_path =stim_name,
            is_image = is_image,
            question = this_question,
            anch1=anchor1,
            anch2 = anchor2,
            stimuli =stimulitype,
            image_video = image_video_type,         
             debug = Constants.images,
             debug2 = Constants.questionsplit,
             number_debug = self.session.vars['stim_order'])
