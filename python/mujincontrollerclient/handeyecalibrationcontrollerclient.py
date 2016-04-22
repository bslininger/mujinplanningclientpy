# -*- coding: utf-8 -*-
# Copyright (C) 2013-2015 MUJIN Inc.
# Mujin controller client for bin picking task

# logging
import logging
log = logging.getLogger(__name__)

# system imports

# mujin imports
from . import planningclient
from . import ugettext as _

class HandEyeCalibrationControllerClient(planningclient.PlanningControllerClient):
    """mujin controller client for hand-eye calibration task
    """
    tasktype = 'handeyecalibration'
    
    def __init__(self, robot, **kwargs):
        """logs into the mujin controller, initializes hand eye calibration task, and sets up parameters
        :param controllerurl: url of the mujin controller, e.g. http://controller14
        :param controllerusername: username of the mujin controller, e.g. testuser
        :param controllerpassword: password of the mujin controller
        :param scenepk: pk of the bin picking task scene, e.g. irex2013.mujin.dae
        :param usewebapi: whether to use webapi for controller commands
        """
        super(HandEyeCalibrationControllerClient, self).__init__(tasktype=self.tasktype, **kwargs)
        self.robot = robot
        
    def ComputeCalibrationPoses(self, camerafullname, numsamples, halconpatternparameters, calibboardvisibility, toolname, targetarea="", samplingmethod=None, patternlinkname="", timeout=3000, **kwargs):
        taskparameters = {'command': 'ComputeCalibrationPoses',
                          'camerafullname': camerafullname,
                          'halconpatternparameters': halconpatternparameters,
                          'patternvisibility': calibboardvisibility,
                          'patternlinkname': patternlinkname,
                          'numsamples': numsamples,
                          'toolname': toolname,
                          'targetarea': targetarea,
                          'debuglevel': 4
                          }
        if samplingmethod is not None:
            taskparameters['samplingmethod'] = samplingmethod
        taskparameters.update(kwargs)
        if self.robot is not None:
            taskparameters["robot"] = self.robot
        result = self.ExecuteCommand(taskparameters, timeout=timeout, usewebapi=True)
        return result
    
    def ComputeStereoCalibrationPoses(self, camerafullnames, numsamples, halconpatternparameters, calibboardvisibility, toolname, targetarea="", samplingmethod=None, patternlinkname="", timeout=3000, **kwargs):
        taskparameters = {'command': 'ComputeStereoCalibrationPoses',
                          'camerafullnames': camerafullnames,
                          'halconpatternparameters': halconpatternparameters,
                          'patternvisibility': calibboardvisibility,
                          'patternlinkname': patternlinkname,
                          'numsamples': numsamples,
                          'toolname': toolname,
                          'targetarea': targetarea,
                          }
        if samplingmethod is not None:
            taskparameters['samplingmethod'] = samplingmethod
        taskparameters.update(kwargs)
        if self.robot is not None:
            taskparameters["robot"] = self.robot
        result = self.ExecuteCommand(taskparameters, timeout=timeout, usewebapi=True)
        return result
    
    def ReloadModule(self, **kwargs):
        return self.ExecuteCommand({'command': 'ReloadModule', 'sceneparams': self.sceneparams, 'tasktype': self.tasktype}, **kwargs)
