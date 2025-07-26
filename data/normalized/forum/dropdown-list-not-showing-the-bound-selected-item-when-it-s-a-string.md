# Dropdown list not showing the bound selected item when it's a string?

## Question

**Jst** asked on 04 Oct 2021

I am filling my drop down from a data table. The Value and the Text are the same string. The Value is also a string that matches the ValueField string. But when the DropDown Renders the value is not selected and just shows a blank. How do I get the selected value to be selected? <TelerikDropDownList Data="@MyVM.ContactFormatList" TextField="@nameof(QuerySelector.ColumnName)" Filterable="true" ValueField="@nameof(QuerySelector.ColumnName)" DefaultText="Select Contact Format" @bind-Value="@MyVM.selectedContactFormat"> </TelerikDropDownList> MyVM.ContactFormatList=list of QuerySelectors public class QuerySelector { public string ColumnName { get; set; } public string Value { get; set; }
} Property in my MyVM public string selectedContactFormat { get; set; }

## Answer

**Marin Bratanov** answered on 05 Oct 2021

Hi, If you have only string values, you can bind the component to a collection of strings, like that: [https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind#primitive-types](https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind#primitive-types) Regards, Marin Bratanov Progress Telerik

### Response

**Jstemper** commented on 07 Oct 2021

I have simplified my code to a simple list of strings and it still will not "select" the bound value. I am filling the lists in the following code: protected override async Task OnInitializedAsync ( ) {
UpdatedLoan. ContactFormatList=await SelectListService.GetSelectListAsync( 10 );
} My razor page looks like this: <TelerikDropDownList Data="@MyVM.ContactFormatList" @bind-Value="@MyVM.ContactFormat"> </TelerikDropDownList> I am also displaying the selected value in the razor page like this: @MyVM.ContactFormat That displays the expected value but the selected value does not show in the dropdown.

### Response

**Marin Bratanov** commented on 07 Oct 2021

Try adding an await InvokeAsync(StateHasChanged); after the data retrieval - it is possible that it actually retuns after OnAfterRender so the component does not re-render anymore. If this does not help, I recommend you open a support ticket and send us a small runnable sample that shows the issue so we can debug, as I am mostly guessing based on a few lines now.
