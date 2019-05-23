# The final goal of this script is to reflect the mesh. e.g. with having only right side of the body you can have the other side as well.
# or you can have the combination of them merged.
#
# =============== File Reader =================
# 1) Exfile reader
# read x
class Node:
    def __init__(self):
        self._number = None

    def set_user_number(self, number):
        self._userNumber = number

    def set_location(self, location):
        self._location = location