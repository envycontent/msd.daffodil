## Script (Python) "testForWidth"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=sl, sr
##title=
##
if sl and sr:
    return "layoutcolumn span-12"
if sl:
    return "last layoutcolumn  span-18"
if sr:
    return "layoutcolumn span-18"
return "layoutcolumn span-24"
