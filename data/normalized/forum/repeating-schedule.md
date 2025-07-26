# repeating schedule

## Question

**Sør** asked on 29 Jun 2021

hi I'm building a system where my users will be able to set up a repeating weekly schedule I'm wondering if there are any good components suitable for this, i was thinking of making it look like the attached image since doing it with buttons, would be hard on my users since there would be 168 of them

## Answer

**Marin Bratanov** answered on 29 Jun 2021

Hi Søren, I think you can make such a layout with a grid - you need a model instnace for each hour with 8 fields - the hour, and flags for monday through sunday. You can then color the cells conditionally with the CellRender event based on their data. If you want extremely fast editing, the Template of each cell will let you attach a click handler for each cell click to toggle the value. Regards, Marin Bratanov Progress Telerik

### Response

**Søren** commented on 30 Jun 2021

is there any way to have it react on hold down & hover over, so i can drag an on/off state accross a day?

### Response

**Marin Bratanov** commented on 30 Jun 2021

If you can attach the desired handlers on the elements you put in the template it could. I am not sure what the desired goal is and whether it would be generally achievable by Blazor only, though. Perhaps you may also want to Follow the implementation of a Spreadsheet component that is also quite suitable for such a task: [https://feedback.telerik.com/blazor/1442151-spreadsheet-component](https://feedback.telerik.com/blazor/1442151-spreadsheet-component) - if you find it suitable, also click the Vote button to raise its priorty.

### Response

**Søren** commented on 30 Jun 2021

essentially it is a weekly schedule where my users should be able to decide which hours the system should be online, e.g. a user might need the system to be online monday 8-17, and off the rest of the time
