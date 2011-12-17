from django.db import models
from urllib import urlopen

class problem( models.Model ):
    number = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=1000)

    description = models.CharField(max_length=1000)
    solution = models.CharField(max_length=1000)
    
    def getSolution( self ):
        ''' find the file '''
        h = open( 'codes/problems/p' + str( self.number ) + '.py' )
        self.solution = '<pre>' + '\n'.join(h.readlines()) + '</pre>'
        return self

    def getDescription( self ):
        y = urlopen( "http://projecteuler.net/problem=" + str( self.number ) ).read().decode()
        self.description = (y[ y.index("<p>"): len(y) - ''.join(reversed(y)).index(">p/<")]).replace(
            '<a href="p','<a href="http://projecteuler.net/p').replace(
            "<img src='p","<img src='http://projecteuler.net/p").replace(
            '<img src="i','<img src="http://projecteuler.net/i').replace(
            "<img src='i","<img src='http://projecteuler.net/i")
        print self.description
        return self

    def _pre_save( self ):
        self.getSolution()
        self.getDescription()

    def _post_save( self ):
        problem.objects.all().delete()
