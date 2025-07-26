# maintain custom data model via Scheduler...or Calendar?

## Question

**che** asked on 09 Jul 2021

Hello, I am trying to decide if I can use either the Calendar or Scheduler control (or even leverage both) for the following problem. We have a data model that represents some forecasted daily values. It is keyed on the date, so there is one unique occurrence/tuple of this class per day. It could perhaps be implemented as a Dictionary<k,v>, where the key is the date or date-string. The users of this UI will want to be able to: 1. See a single- or multi-month "calendar" of the forecast values in the main view of the control (perhaps like customized appointments in the Scheduler?) 2. Select one or multiple days (like you can do in the Calendar control, not really in the Scheduler?) and then be able to enter or edit the forecast values for the selected set of days. 3. Put the entire "calendar" (whatever month(s) are visible at the moment) into edit mode where the date cells use a template to edit the model. So, the Telerik Calendar has the ability to select by date(s) - rather than appointments. The Scheduler naturally comes with a UI that is closer to what we need to display a complex object in the day's cell. On the other hand, the Scheduler is build around the concept of appointments and tasks, which is not really how our users will be thinking about the data. I'm playing around with the Calendar right now and able to get some data into the template, but it looks like garbage right now because the space is obviously constricted. I have a long way to go, so I'm hoping to find some samples or ideas at least. <TelerikCalendar SelectionMode="@CalendarSelectionMode.Multiple" ValueChanged="@MultipleSelectionChangeHandler" @ref="@multipleSelectionCalendar"> <MonthCellTemplate> <div style="border-color:black; border-width:2px"> @context.Day
@{
string date=context.ToString("yyyyMMdd");
if (forecasts.ContainsKey(date))
{ <div> Forecast : forecasts[date].Forecast </div> }

} </div> </MonthCellTemplate> </TelerikCalendar> Thanks a lot!!

## Answer

**Marin Bratanov** answered on 11 Jul 2021

Hi, From what I can get from the goals, I think that the calendar with the day template is the way to go - it will let you put custom information in there, you can add a button or other element (perhaps the very custom info element) that the user can click to edit, and perhaps you could pop a window open to provide additional editing capabilities. That also lets you use the built-in date selection too. Finally, you can add some CSS to override the default calendar size to increase it. Here is an example of that (and the basic concept I described above): <TelerikCalendar SelectionMode="@CalendarSelectionMode.Multiple" Class="large-cells"> <MonthCellTemplate> <div style="border-color:black; border-width:2px"> @context.Day <span @onclick:stopPropagation="true"> @* prevent click from going to the cell to affect selection *@<TelerikButton Icon="edit" Class="k-flat" OnClick="@( _=> ShowEditingWindow(context) )"> </TelerikButton> </span> </div> </MonthCellTemplate> </TelerikCalendar> <TelerikWindow @bind-Visible="@editorVisible"> <WindowTitle> Edit </WindowTitle> <WindowActions> <WindowAction Name="Close" /> </WindowActions> <WindowContent> Add editors here for the desired model, now we will simply render the chosen date: @editedModelMimic </WindowContent> </TelerikWindow> @code{
bool editorVisible { get; set; }
DateTime editedModelMimic { get; set; }
void ShowEditingWindow(DateTime date)
{
editedModelMimic=date; // get the whole model or otherwise prepare editing

editorVisible=true;
}
} <style>.large-cells.k-calendar,.large-cells.k-calendar.k-calendar-view { width: 800px; /*match this to the number of calendar views and cell sizes you want*/ height: 550px;
}.large-cells.k-calendar.k-month td,.large-cells.k-calendar.k-month.k-calendar-td,.large-cells.k-calendar.k-calendar-monthview td,.large-cells.k-calendar.k-calendar-monthview.k-calendar-td { width: 100px; height: 100px;
}.large-cells.k-calendar-content.k-link { width: 100%; height: 100%; display: block;
} </style> Regards, Marin Bratanov Progress Telerik

### Response

**chesk345** commented on 13 Jul 2021

Thank you, Marin...this provides a good start! I am working with it now, and I'm hopeful I can get it to do all we need. One thing; I found that I needed to upgrade the project from netstandard2.1 to net5 for it to Publish successfully to the file system. I'm just curious if that makes sense with the current Telerik build (2.25.0)..?

### Response

**Marin Bratanov** commented on 13 Jul 2021

It should not be required if this is in a razor class library. If this is a WebAssembly project - it will be required, MS dropped support for .NET Core 3.2.1 which made WASM apps a netstandard2.1 app, it is now a .net5.0 app. You can see more about this here [https://docs.telerik.com/blazor-ui/upgrade/framework-versions](https://docs.telerik.com/blazor-ui/upgrade/framework-versions)

### Response

**chesk345** commented on 13 Jul 2021

Thank you again, Marin...
