'''
Simple game
1. type a word
2. react
3. slash command
4. press a button
'''
class SlackGame:

    WELCOME_TEXT = {
        'type' : 'section',
        'text' : {
            'type':'mrkdown',
            'text' : (
                'Welcome to my game! \n\n'
                'You will have serveral tasks to complete, each of which require a different interaction with the bot!\n'
                'Let\'s begin with question 1'
            )
        }
    }

    DIVIDER = {'type' : 'divider'}

    # dictionary containing
        # user_id
        # progress in the game (init certain elements only if they progressed to the correct stage)

    # dictionary (database) containing
        # id : auto incrementing
        # text : all elements for propper formatting and question
        # question_reaction_type : slash / text / react
        # expected answer : (message, react type, slash url)

    def __innit__(self, channel_id, user_id, mysql):
        #if user_id not _is_playing()
            #greet user
            #make entry in db (cls)
            #ask first question
        pass

    def message_handler(self, payload):
         # if expected answer from  question_db with id of user_progress
            # proceed with next task
        # else
            # print not understood
        pass

    def slash_handler(self, payload):
        # if expected answer from  question_db with id of user_progress
            # proceed with next task
        # else
            # print not understood
        pass

    def react_handler(self, payload):
         # if expected answer from  question_db with id of user_progress
            # proceed with next task
        # else
            # print not understood
        pass

    def _send_task(self, tasknum):
        #send task from dictionary of tasks
        pass

    def _add_in_db(cls, user_id):
        #if entry not exists
            # make new entry
        #elif not already playing
            # change status to playing
        pass

    def _user_progress(cls, user_id):
        #if entry not exists
            #return -1
        #else
            #return progress (0 = not playing)
        pass

