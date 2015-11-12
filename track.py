from datetime import timedelta, datetime

from timing import Timing


class Track(Timing):
    id = 0

    def __init__(self):
        
        """Constructor Function"""
        
        super(Track, self).__init__()
        Track.id += 1
        self.talks = {}
        self.talk_list = Track.extract_input()

     
    def extract_input():
        
        """Function to extract input from the text file"""
        
        __talks = {}
        lines = []
        try:
            lines = [line.strip() for line in open('test.txt')]
        except FileNotFoundError as e:
            print('File Not Found', e)
        for line in lines:
            title, minutes = line.rsplit(maxsplit=1)
            try:
                minutes = int(minutes[:-3])
            # negative indexing raises error, so it means it's lightning
            except ValueError:
                minutes = 5
            __talks[line] = minutes
        return __talks

    def get_talks(self, start_talk, end_talk):
        
        """Function for get talk"""
        
        start = timedelta(hours=start_talk)
        for key, value in list(self.talk_list.items()):
            prev = start + timedelta(minutes=int(value))
            if prev <= timedelta(hours=end_talk):
                self.talks[(datetime.min + start).strftime('%I:%M %p')] = key
                self.talk_list.popitem()
                start += timedelta(minutes=int(value))
        return self.talks

    def show_output(self):
        
        """Function to print the output of track id,Lunch and networking event"""
        
        while not len(self.talk_list) is 0:
            print('Track %s' % Track.id)
            self.__prepare_output(9, 12)
            print('%s - %s' % (self.lunch, 'Lunch'))
            self.__prepare_output(13, 17)
            print('%s - %s' % (self.day_end, 'Networking Event'))
            Track.id += 1

    def __prepare_output(self, start, end):
        
        """Function to print remaining time and tile other than Lunch and networking event"""
        
        for time, title in sorted(self.get_talks(start, end).items()):
            print(time, '-', title)
        # clear previous entries
        self.talks.clear()


if __name__ == '__main__':
    a = Track()
    a.show_output()
