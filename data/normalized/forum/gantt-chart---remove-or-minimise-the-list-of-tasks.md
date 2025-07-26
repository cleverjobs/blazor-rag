# Gantt Chart - remove or minimise the list of tasks

## Question

**haP** asked on 20 Dec 2022

Hi I have a use case whereby I just need the graphic representation of the Gantt only (i.e. not the list of tasks on the left). I have tried leaving the GanttColumn property empty (no GanttColumn items in it) but it still displays the section of the control which is just blank. I can get the view I want by then using the slider to adjust the width of that section till the gantt graphical part covers the entire control (see attached image) What I would like to be able to do is to be able to do that through code not by moving the slider manually. Is there a way - I assume there must be some css class I could adjust the width of somewhere given how flexible these components seem to be. Thanks

## Answer

**haPartnerships** answered on 20 Dec 2022

OK - clearly missed the very well labelled TreeListWidth property which set to 0px works for what I needed!!!
