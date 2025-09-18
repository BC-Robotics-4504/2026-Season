
import wpilib


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        pass

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        pass
    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        pass

    def testInit(self):
        """This function is called once each time the robot enters test mode."""
        pass

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
