# DropDownList - OnChange not firing when selecting the "default" entry

## Question

**Kas** asked on 01 Jul 2020

Hi, when setting DropDownList's DefaultText (e.g. to a "none" string) then the component displays an additional entry which stands for a null/default value (in other words: it acts as a clear button). But the OnChange event does not fire when selecting that entry. Using: Telerik.UI.for.Blazor.Trial (2.14.1) Regards Kasimier Buchcik

## Answer

**Marin Bratanov** answered on 01 Jul 2020

Hello Kasimier, Could you reproduce this issue with 2.15.0 and the following snippet as base? I am asking this because it seems to work as expected for me and I am also attaching a short video that shows my test so you can confirm if I am missing something. At the moment, my best guess is that the data source has the default value somewhere which can interfere with the DefaultText behavior. @result
<br /> from the model: @MySelectedItem
<br />
<TelerikDropDownList Data="@MyList" OnChange="@MyOnChangeHandler" @bind-Value="@MySelectedItem" DefaultText="select something">
</TelerikDropDownList>

@code { string result; string MySelectedItem { get; set; }="second"; void MyOnChangeHandler ( object theUserInput ) { string val=theUserInput as string;
result=string.Format( "The user selected: {0}", val !=null? val : "NULL WHICH IS DEFAULT FOR STRING" );
} protected List<string> MyList=new List<string>() { "first", "second", "third" };
} Regards, Marin Bratanov

### Response

**Kasimier Buchcik** answered on 02 Jul 2020

My bad, the OnChange event of the DropDownList *does* fire fine. The bug was on my side: my tiny helper which resolves the actual selected item by key was not prepared for a value of null yet. Thanks & sorry for the inconvenience. Regards Kasimier Buchcik
