# Customizing Column Title Displayed in Popup Editor

## Question

**che** asked on 16 Jul 2021

Hello, I have a grid with nested columns. The column's "child header" Title is displayed in the label of its corresponding editor in the popup. However, in my case, the child header titles are not unique without the "parent" header Titles. Can I prepend the "parent header" Title in the labels in the popup? A screenshot is attached. Note the red and green label pairs are identical in the popup, so the user can't distinguish what the data attributes are. Thanks again!

## Answer

**chesk345** answered on 19 Jul 2021

PS - For my needs, I just discovered a simpler solution. With the HeaderTemplate, I can use the "full" name as the Title (which is used by the editor) while displaying the abbreviated text in the grid through the template. I don't need to define extra columns. Sample and screenshot are now attached...

### Response

**Marin Bratanov** commented on 19 Jul 2021

That's a neat idea, I converted this comment to an answer to improve its visibility. If you could post a small code snippet for everyone else to see, that would be grand! Thanks!

### Response

**chesk345** commented on 21 Jul 2021

I attached sample razor code and a screenshot.

### Response

**Marin Bratanov** commented on 21 Jul 2021

Awesome, thanks!

### Response

**Marin Bratanov** answered on 17 Jul 2021

Hi, The grid popup editing uses the column titles for titles for their labels, so if you cannot make them unique in the column definitions (e.g., add some abbreviation or other info in brackets after the current titles), you can change them dynamically while in edit mode in a fashion similar to this. Regards, Marin Bratanov Progress Telerik

### Response

**chesk345** commented on 19 Jul 2021

For each of the model properties in question, I implemented two columns with opposing toggles on their visibility. Columns visible in normal mode have the normal Title, and no editor template, while those visible in edit mode have the customized Title and the editor template. Thanks for your assistance.
