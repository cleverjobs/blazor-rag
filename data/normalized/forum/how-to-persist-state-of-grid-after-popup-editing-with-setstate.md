# How to persist state of grid after popup editing with SetState ?

## Question

**mah** asked on 13 Jun 2022

I have a grid with a hierarchy grid inside it. I can expand each row in the master grid but when I edit one row (I use popup mode to edit) after closing the popup all rows collapse. I try to save the grid state and then set the state in the OnStateChangeHandler event but its not working correctly it seems that the grid state has been set after closing popup by an unknown event.
