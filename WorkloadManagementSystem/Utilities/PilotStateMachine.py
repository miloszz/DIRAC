""" Transformation Files state machine (LHCb specific)
"""

__RCSID__ = '$Id$'

from DIRAC.ResourceStatusSystem.PolicySystem.StateMachine         import State
from LHCbDIRAC.ProductionManagementSystem.Utilities.StateMachine  import LHCbStateMachine

class PilotStateMachine( LHCbStateMachine ):
  
  def __init__( self, state ):
    
    super( PilotStateMachine, self ).__init__( state )
    
    self.states = {
                   'Deleted' : State( 8 ),
                   'Done' : State( 7 ), # final state
                   'RunningJob': State( 6, ['Done', 'Matching', 'Failed'] ),
                   'Matching' : State( 5, ['RunningJob', 'Failed'] ),
                   'Configuring' : State( 4, ['Matching', 'Failed'] ),
                   'Installing' : State( 3, ['Configuring', 'Failed'] ),
                   'Landed' : State( 2, ['Installing', 'Failed'] ),
                   'Submitted' : State( 1, ['Landed', 'Failed'] ),
                   'Failed' : State( 0 ), # final state
                   }