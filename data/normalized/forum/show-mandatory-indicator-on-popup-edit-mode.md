# Show mandatory indicator on popup edit mode

## Question

**Kev** asked on 12 Nov 2020

Sorry if this has been asked before but how can I show a mandatory indicator (a red *) after Title for each mandatory field in popup edit mode? Thanks Kevin

## Answer

**Marin Bratanov** answered on 12 Nov 2020

Hello Kevin, There are three approaches you can take: Keep using the grid popup edito as-is - when the user clicks Save or types an invalid value in an input (such as clear a required input), validation messages will pop up immediately to notify them. You can check this in our poup editing online demo - try deleting the Name. Use the EditorTemplate of the desired column to add the marker you require next to your customized editor (input). Create a custom popup form that will let you define the layout and markings as desired. Regards, Marin Bratanov
