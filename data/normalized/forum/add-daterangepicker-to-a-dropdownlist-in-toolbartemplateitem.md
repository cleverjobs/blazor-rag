# Add DateRangePicker to a DropDownList in ToolBarTemplateItem

## Question

**Jim** asked on 13 Aug 2021

Hi, I need to have a DateRangePicker to allow a user to select a date range in the Toolbar. Ideally, I want to implement this in a DropDownList with the Placeholder text of "All Dates". When the drop down list is clicked, the DateRangePicker is shown and a user can select a range of dates which will then show after focus is lost. The user should be able to select "All Dates" again so no "date range" is selected to send to my API. See attached screen show. Any help is much appreciated! Jimmy <ToolBarTemplateItem> <TelerikDropDownList Data="@dateLookupModel" TextField="LookupTextField" ValueField="LookupValueField" @bind-Value="@dateLookupType" width="125px"></TelerikDropDownList> </ToolBarTemplateItem> <ToolBarSeparator /> <ToolBarTemplateItem> Dates: <TelerikDateRangePicker Class="daterangepicker-no-labels" @bind-StartValue="@StartValue" @bind-EndValue="@EndValue"></TelerikDateRangePicker> </ToolBarTemplateItem> <ToolBarSeparator /> Code: public DateTime? StartValue { get; set; }=new DateTime(DateTime.Today.Year, DateTime.Today.Month, DateTime.Today.Day); public DateTime? EndValue { get; set; }=new DateTime(DateTime.Today.Year, DateTime.Today.Month, DateTime.Today.Day); private FilterDate dateLookupType { get; set; }=FilterDate.AllDates; private List<LookupItemModel<FilterDate>> dateLookupModel { get; set; }=new(); foreach (var value in Enum.GetValues(typeof(FilterDate))) { dateLookupModel.Add(new LookupItemModel<FilterDate>() { LookupTextField=((FilterDate)value).GetAttribute<DisplayText>().Text, LookupValueField=(int)value, LookupSortValue=((FilterDate)value).GetAttribute<OrderAttribute>().Order }); dateLookupModel.Sort((x, y)=> x.LookupSortValue.CompareTo(y.LookupSortValue)); }

## Answer

**Marin Bratanov** answered on 14 Aug 2021

Hello Jimmy, The desired UX seems quite complicated and I can suggest you consider putting it inside a Window component that you show on click of a simple toolbar button. This will give you a lot of flexibility in implementing your logic, rendering and customizing the layout without being constrained by a small space in the toolbar. If I understand you correctly, you want to have the entire DateRangePicker be inside the "All Dates" item in the dropdownlist. If this is the requirement, I'm afraid that it isn't going to be possible - even if you use the ItemTemplate to render a range picker in one of the items in the dropdown, interacting with the popup of one of these components is very likely to hide the other and thus the UX could suffer a lot. Regards, Marin Bratanov Progress Telerik

### Response

**Jimmy** commented on 14 Aug 2021

Thanks Martin, I had a feeling this would be the reasonable way to approach this. What I'm really looking for is a date range picker that is in the Toolbar as a menu item. If blank, no date range is passed to my API. If a date range exists, that date range is passed to my API. A requirement would be to show what date range the user has selected in the Toolbar. If you have any more ideas or suggestions how to best implement this, I'd greatly appreciate it. Jimmy

### Response

**Marin Bratanov** commented on 15 Aug 2021

Jimmy, while I am still not sure what the exact goal is, I have the feeling that trying to cramp in so much functionality into so few elements would require that some actions become ambiguous such as dropdown selection would sometimes have to do one thing, other times another, some elements feel like they are editors, but other times just information blocks. That can not only be confusing for the end user, it also becomes harder to implement from code perspective. That's why I was thinking that perhaps dedicating a bit more space (such as its own dialog or something like that) would be a better approach to solve this. Alternatively, you can look into a bunch of if-blocks to render different contents based on flags you raise and lower in the view model, and you can also use those flags to determine what should be present in the API call for saving the info. You can even switch out different toolbar items with their Visible parameter based on those flags. The main task in front of you would be rather deciding what those flags are, and when to toggle them. I am also getting the feeling that you are using the toolbar as a collection of inputs, and perhaps the Form component would be better suited for that task (you can also customize its items through their template to put special editors).

### Response

**Jimmy** commented on 15 Aug 2021

Hi Martin, Thanks for the quick reply and information! You are correct, I'm using the toolbar as a collection of inputs that are used as filters to pass to my API when a user searches for an item. I have some design flexibility, but unfortunately, my hands are tied in the fact that I need to keep the new Blazor WebAssembly app close in look and functionality as that of the WinForms app that it will eventually replace. This decision was made at a higher level to make the transition for users who use the application easy. I've included a screen shot of the toolbar with a collection of inputs as "filters" that are used when the search button is pressed. Hopefully this will give you a better idea of what I'm trying to achieve. Regards, Jimmy

### Response

**Marin Bratanov** commented on 15 Aug 2021

Jimmy, I think that you may not need a toolbar component at all, just add the elements/components you need one next to the other. Or, maybe, you may also want to Vote for and Follow a Filter Component implementation: [https://feedback.telerik.com/blazor/1445600-filter-component](https://feedback.telerik.com/blazor/1445600-filter-component)

### Response

**Jimmy** commented on 16 Aug 2021

Thanks for all of your help, Martin! I'm going to proceed and give the Filter Component a vote. Thanks, Jimmy
