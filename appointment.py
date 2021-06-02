"""Driver: Sana Hassan
Navigator:  Asad Raheem
"""

class Appointment:
    """  This program checks for scheduling conflicts, it holds onto information about an appointment and can detect conflicts
    with other appointments

   


    """
    def __init__(self, name:str, start:(int, int), end: (int, int)):
        """ purpose: create an appointment with the given name, start and end times
        
        
        parameters:
        
        
            name: str, takes in the name of the appointment,
            for example 'Sales Brunch'
            start:  (int, int) takes in the hour and minute of the appointment    
            end:
            
        *side effects
        modify the attributes self.name, self.start, and self.end by storing the parameters in the attributes of the same name"""  
        
        
        
        self.name = name
        self.start = start
        self.end = end
    def overlaps(self, other):
    
        """
        *purpose: check for scheduling conflicts
    
        *paramaters
        other:  Appointment.  the appointment to check for conflicts
        
        *returns
        return True if appointments overlap False otherwise
        
        """
        
        
        return (self.start <= other.start and other.start <= self.end
                or self.start < other.end and other.end <= self.end)
        
