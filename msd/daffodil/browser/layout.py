from zope.interface import implements
from zope.publisher.browser import BrowserView

from msd.melipona.browser.interfaces import IMeliponaLayoutPolicy


class MeliponaLayoutPolicy(BrowserView):
    """A view that gives access to various layout related functions.
    """

    implements(IMeliponaLayoutPolicy)

    
    def get_content_column_class(self, column_left, column_right):
        """Get the classes for the middle column
           calculating the width from the presence of left or right cols
        """
        
        if not column_right and not column_left:
            return "layoutcolumn span-24"
        if column_right and not column_left:
            return "layoutcolumn span-18"
        if not column_right and column_left:
            return "last layoutcolumn span-18"
        return "layoutcolumn span-12"
        
    def get_column_left_class(self):
        """Return classes for the left column    
        """
        
        return "layoutcolumn span-6"

    def get_column_right_class(self):
        """Return classes for the right column
        """
        
        return "last layoutcolumn span-6"

    