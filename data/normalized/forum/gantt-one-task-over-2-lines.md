# [Gantt] One task over 2 lines

## Question

**Val** asked on 25 Mar 2025

Hello Telerik team, I'm new in Blazor environment, and I would like to use a mix of controls in order to display data. The goal is to have several columns and rows (like DataGrid control),: columns represent calendar days (like Scheduler control); rows representing "stations" [tasks] (like Gantt control); core of the control (crossing between rows and columns) represented as chipset (my data). In fact, I think the best control could be the Gantt control because of its structure and content, but I have one issue with that: I won't be able to put an item (chipset) over 2 rows. Unfortunely, I can't provide you any picture of what I want because of my company restrictions. Are you able to help me and provide me some advices? Many thanks, Valentin M.

## Answer

**Anislav** answered on 27 Mar 2025

TelerikGrid does not support items to occupy multiple rows or columns (rowSpan or colSpan). However, TelerikGridLayout does provide this functionality, which might be a suitable alternative. I have prepared a sample using TelerikGridLayout where tasks span multiple columns (representing dates). If you need the same behavior for rows, a similar approach can be applied. Here is the link to my example [https://blazorrepl.telerik.com/cpYHmBbK35I5JCzz54.](https://blazorrepl.telerik.com/cpYHmBbK35I5JCzz54.) Edit: I generated another sample where tasks are grouped vertically by stations instead of horizontally by dates: [https://blazorrepl.telerik.com/cfuxnPwE13cjmLEv38](https://blazorrepl.telerik.com/cfuxnPwE13cjmLEv38) Please note that this code does not support overlapping tasks assigned to the same station on the same date. While this can be handled, it requires a more efforts. Regards, Anislav Atanasov

### Response

**Valentin** commented on 31 Mar 2025

Hello Anislav, Thank you for your feedback and the provided sample code. If I understand well, you are using GridLayoutItem control with the property ColumnSpan. For my usecase, I will be able to use RowSpan, in order to display the same item over 2 rows, right? The display you have built it's what I want. And for example, the Quality Check item has to be over 2 rows (2 stations). In addition, will I be able to customize the style of each component to display them as a style or not? (I'm coming from XAML and WPF, I guess it's not the same way). Many thanks! Valentin.

### Response

**Anislav** commented on 31 Mar 2025

Yes, you should be using RowSpan. I have updated my answer to include an example demonstrating this. From my perspective, the TelerikGridLayout is a relatively basic layout component that offers customizations such as alignment, width, spacing, and the ability to apply a CSS class. However, most of the styling will need to be managed through CSS, as it doesn't provide the polished UI features found in components like Gantt and Scheduler. Regards, Anislav Atanasov

### Response

**Valentin** commented on 31 Mar 2025

Dear Anislav, Many thanks for the sample code. I think with your example and some additional style, I will be able to create something pretty and perfectly functionnal (the functionnality is quite simple btw). I have taken into account your note in your edited post, I think it won't be a blocking point because I don't need to do that. In fact, I want to have 2 rows per station, and sometimes, an item will take the 2 rows and sometimes, 2 items will be associated to the station (one per row for the same day). I think the GridLayout will allow me this configuration. One last question: is vertical center aligment be possible? For example, if the station is represented by 2 rows, will I be able to vertically align (center) the name of the station between the 2 rows? Thank you! Valentin M.

### Response

**Anislav** commented on 31 Mar 2025

I updated the link to the second sample in my answer, as there was an issue with the first one. Additionally, I added VerticalAlign="GridLayoutVerticalAlign.Center" to the TelerikGridLayout, which will vertically align the cells. Regards, Anislav Atanasov

### Response

**Valentin** commented on 01 Apr 2025

Many thanks Anislav! I can imagine what will develop thanks to your explanations.
