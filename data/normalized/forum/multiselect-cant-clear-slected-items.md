# Multiselect, cant clear slected items!!!

## Question

**Dea** asked on 26 Apr 2023

This is driving me nuts. I have tried the .clear() and I have tried re-init the object. Nothing seems to clear this from the UI that the user sees. on the razor page: <TelerikMultiSelect @ref="DDLFil1" Class="my-multiselect" Data="@DDLFil1List" TextField="Result" TItem="DDLList" ValueField="Result" TValue="string" Placeholder="Select the items you need" AutoClose="false" Filterable="true" ClearButton="true"> <MultiSelectSettings> <MultiSelectPopupSettings Height="500px" /> </MultiSelectSettings> <HeaderTemplate> <label style="padding: 4px 8px;"> <TelerikCheckBox TValue="bool" Value="@DDLFil1_IsAllSelected()" ValueChanged="@( (bool v)=> DDLFil1_ToggleSelectAll(v) )"></TelerikCheckBox> &nbsp;Select All </label> </HeaderTemplate> </TelerikMultiSelect> In the CS behind the code page: public TelerikMultiSelect<DDLList, string> DDLFil1 { get; set; } // Ctrl on the webpage private bool blnHideDDLFil1 { get; set; }=true; string DDLFil1Lbl=""; List<DDLList> DDLFil1List=new List<DDLList>(); string? _DDLFil1SelectedId; string DDLFil1SelectedId { get { return _DDLFil1SelectedId; } set { _DDLFil1SelectedId=value; } } List<string> DDLFil1Values { get; set; }=new List<string>(); List<string> DDLFil1Results { get; set; }=new List<string>(); Clearing code: if (DDLFil1.Value !=null) { if (DDLFil1.Value.Count()> 0) { // Items have been selected! DDLFil1.Value.Clear(); }; }; How does one Clear the selected items for the user to re-use without having them to unselect each item. You have a ClearSelectAll Button on the Control. sometimes hard for the user to see it with multiple items selected. Would be nice if i could call that in code!!! DDLFil1.ClearSelectedAll(); I really need this feature. Thanks

## Answer

**Deasun** answered on 25 May 2023

Svetoslav answered it.

### Response

**Radko** answered on 27 Apr 2023

Hi Deasun, To clear the value within the MultiSelect, you should provide a new collection reference. You can read more about this here: MultiSelect - Refresh Data - New Collection Reference. Here is an example of this: [https://blazorrepl.telerik.com/cxkowrFQ37qkCaXM52](https://blazorrepl.telerik.com/cxkowrFQ37qkCaXM52) Regards, Radko Progress Telerik

### Response

**Deasun** commented on 09 May 2023

That example come sup blank!. Tried FireFox and Chrome latest versions.

### Response

**Radko** answered on 12 May 2023

Hello Deasun, Could you try clearing the cache of your browser? Although unlikely, as you have attempted to load it in two different browsers, this could potentially be the reason for the issue. It loads correctly on my end. Anyhow, I'm sharing the code from the snippet directly for you to inspect: <TelerikMultiSelect Data="@Countries" Id="countries" Width="100%" @bind-Value="@Values" Placeholder="Enter Balkan countries, e.g., Bulgaria">
</TelerikMultiSelect>

@string.Join( ", ", Values)

<hr/>

<TelerikButton OnClick="@ClearMultiSelectValue">Clear MultiSelect value </TelerikButton>

@code { void ClearMultiSelectValue ( )=> Values=new List<string>();

List<string> Countries=new List<string>();
List<string> Values=new List<string>(); protected override void OnInitialized ( ) {
Countries.Add( "Albania" );
Countries.Add( "Bosnia & Herzegovina" );
Countries.Add( "Bulgaria" );
Countries.Add( "Croatia" );
Countries.Add( "Kosovo" );
Countries.Add( "North Macedonia" );
Countries.Add( "Montenegro" );
Countries.Add( "Serbia" );
Countries.Add( "Slovenia" ); base.OnInitialized();
}
} Regards, Radko Progress Telerik

### Response

**Deasun** commented on 22 May 2023

Sorry for taking so long to respond. Being very busy. Sense I am getting my List of items from a DB would that mean I would have to re-init the MSDDL from the DB call again? Is Values=new List<string>() equivlient to my: List<string> DDLFil1Values { get; set; }=new List<string>(); OR List<DDLList> DDLFil1List=new List<DDLList>(); I was under the understanding that; 1] DDLFil1List is where the DB drops its listin of items which is what is displayed to the user to select from. 2] DDLFil1Values and this was where the users selected items was stored. IS that not correct? I thought if I cleared the items in DDLFil1Values then the object on the screen would clear. But it doesnt seem to for me.

### Response

**Deasun** commented on 22 May 2023

Ok I have tried to create a REPL of how I am set up. And then use your example to clear the UI object. It does not work. Also tried the comment out code, that didnt work either. What am I not picking up here? <h1> Hello, Telerik REPL for Blazor! </h1> <TelerikMultiSelect @ref="DDLFil1" Class="my-multiselect" Data="@DDLFil1List" TextField="Result" TItem="DDLList" ValueField="Result" TValue="string" Placeholder="Select the items you need" AutoClose="false" Filterable="true" ClearButton="true"> <MultiSelectSettings> <MultiSelectPopupSettings Height="500px" /> </MultiSelectSettings> <HeaderTemplate> <label style="padding: 4px 8px;"> <TelerikCheckBox TValue="bool" Value="@DDLFil1_IsAllSelected()" ValueChanged="@( (bool v)=> DDLFil1_ToggleSelectAll(v) )"></TelerikCheckBox> &nbsp;Select All </label> </HeaderTemplate> </TelerikMultiSelect> <TelerikButton OnClick="@ClearMultiSelectValue"> Clear MultiSelect value </TelerikButton> @code { void ClearMultiSelectValue()=> DDLFil1Values=new List <string> (); //void ClearMultiSelectValue() //{ // List <DDLList> genDDLItems=new List <DDLList> (); // genDDLItems=getDDLItems(); // DDLFil1List=genDDLItems.Select(s=> new DDLList { Result=s.Result, Value=s.Value }).ToList(); //} public TelerikMultiSelect <DDLList, string> DDLFil1 { get; set; } // Ctrl on the webpage private bool blnHideDDLFil1 { get; set; }=true; string DDLFil1Lbl=""; List <DDLList> DDLFil1List=new List <DDLList> (); string? _DDLFil1SelectedId; string DDLFil1SelectedId { get { return _DDLFil1SelectedId; } set { _DDLFil1SelectedId=value; } } List <string> DDLFil1Values { get; set; }=new List <string> (); List <string> DDLFil1Results { get; set; }=new List <string> (); protected override void OnInitialized() { List <DDLList> genDDLItems=new List <DDLList> (); genDDLItems=getDDLItems(); DDLFil1List=genDDLItems.Select(s=> new DDLList { Result=s.Result, Value=s.Value }).ToList(); base.OnInitialized(); } bool DDLFil1_IsAllSelected() { return DDLFil1Values.Count==DDLFil1Results.Count; } void DDLFil1_ToggleSelectAll(bool selectAll) { if (selectAll) { DDLFil1Values=new List <string> (DDLFil1Results); } else { DDLFil1Values=new List <string> (); }; } public static List <DDLList> getDDLItems() { List <DDLList> DLLItems=new List <DDLList> (); string strCMDToRun=""; try { DDLList ResultRow; ResultRow=new DDLList(); ResultRow.Result="Vader"; ResultRow.Value=1; DLLItems.Add(ResultRow); ResultRow=new DDLList(); ResultRow.Result="Tarkin"; ResultRow.Value=2; DLLItems.Add(ResultRow); ResultRow=new DDLList(); ResultRow.Result="Luke"; ResultRow.Value=3; DLLItems.Add(ResultRow); ResultRow=new DDLList(); ResultRow.Result="Leia"; ResultRow.Value=4; DLLItems.Add(ResultRow); } catch (Exception ex) { string strErrMsg="Error Msg: " + ex.Message + Environment.NewLine + " <br> "; }; return DLLItems; } public class DDLList { public string? Result { get; set; } public int Value { get; set; } } }

### Response

**Svetoslav Dimitrov** commented on 25 May 2023

Hello Deasun, To achieve the desired behavior you must add the @bind-Value syntax and assign the DDLFil1Values to it. I have modified the code snippet you sent (REPL link) to us and clicking the Clear button resets the value as expected. Regards, Svetoslav

### Response

**Deasun** commented on 25 May 2023

can you post that snippet here in the forums? The links to REPL keep coming up blank for me when I click on it.

### Response

**Deasun** commented on 25 May 2023

Thanks for the answer. Thats what I was missing. :)
