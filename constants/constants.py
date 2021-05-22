from dataclasses import *

all_courses_kinds = {"SimpleLicence": SimpleLicence,
             "DoubleLicence": DoubleLicence,
             "Prepa": Prepa}

all_event_kinds = {"Accepted": AcceptEvent,
                   "UserRefused": UserRefuseEvent,
                   "SchoolRefused": SchoolRefuseEvent,
                   "Waiting": WaitingListEvent,
                   "Proposition": PropositionEvent}