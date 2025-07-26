# Can't get the Dropdown/Combobox ValueField value with as an additional parameter

## Question

**Chr** asked on 26 Oct 2023

Some important background first. There is a lot to share but its important because you'll have a lot of question about why I'm doing some things. My model is a single, self-referencing table holding hierarchical data. I have three fields: "TaxonomyId", "Name", "ParentId". Taxonomy Id is my ValueField and Name is the TextField. Currently the hierarchy is limited to 5 levels. The previous dropdown filters the next based on the selection. Names are unique in a single hierarchy but not across hierarchies. Clear as mud? LOL I have separate Lists I use as models for each of the dropdown lists to be cascading through the single hierarchy. I can't use a single table model because each dropdown uses the same model. It appears to overwrite the previous selection and I need to keep track of all the selections. Those lists are bound to each ddl to display the list of Names. So, to make the dropdowns cascade, I call my GetNextLevel() method for the OnChange() event. I tried ValueChange() but firing on every keystroke seemed to cause some UI performance issues. May have just been my ignorance. Anyway, I pass the level (1-5) and the bound value (Name) to get the next ddl values. All this works perfect. Now to the ask. I'm trying to get the ValueField (TaxonomyId) and pass it to GetNextLevel(). I can pass the event args but that only gives me the selected value and I also need the level (which ddl was clicked). If I could send level and the ValueField I would be "golden". Now the code. Here are my ddls <div> <TelerikFloatingLabel Text="Level 1"> <TelerikComboBox Class="justification" AllowCustom="true" Data="@L1" ClearButton="false" TextField="Name" ValueField="TaxonomyId" @bind-Value=@L1Value OnChange="@(GetNextLevelTest)"> </TelerikComboBox> </TelerikFloatingLabel> </div> @if (!String.IsNullOrEmpty(L1Value))
{ <div> <TelerikFloatingLabel Text="Level 2"> <TelerikComboBox Class="justification" @ref="TestRef" id="L2" AllowCustom="true" Data="@L2" ClearButton="false" TextField="Name" ValueField="TaxonomyId" @bind-Value=@L2Value OnChange="@(()=> GetNextLevel(L2Value, 2))"> </TelerikComboBox> </TelerikFloatingLabel> </div> }

@if (!String.IsNullOrEmpty(L2Value))
{ <div> <TelerikFloatingLabel Text="Level 3"> <TelerikComboBox Class="justification" Data="@L3" AllowCustom="true" TextField="Name" ClearButton=false ValueField="TaxonomyId" @bind-Value="@L3Value" OnChange="@(()=> GetNextLevel(L3Value, 3))"> </TelerikComboBox> </TelerikFloatingLabel> </div> }

@if (!String.IsNullOrEmpty(L3Value))
{ <div> <TelerikFloatingLabel Text="Level 4"> <TelerikComboBox Class="justification" Data="@L4" AllowCustom="true" TextField="Name" ClearButton=false ValueField="TaxonomyId" @bind-Value="@L4Value" OnChange="@(()=> GetNextLevel(L4Value, 4))"> </TelerikComboBox> </TelerikFloatingLabel> </div> }

@if (!String.IsNullOrEmpty(L4Value))
{ <div> <TelerikFloatingLabel Text="Level 5"> <TelerikComboBox Class="justification" Data="@L5" AllowCustom="true" ClearButton="false" TextField="Name" ValueField="TaxonomyId" @bind-Value="@L5Value" OnChange="@(()=> GetNextLevel(L5Value, 5))"> </TelerikComboBox> </TelerikFloatingLabel> </div> } Here is the GetNextLevel method. This is more for your edification as I don't think it will impact the answer? A lot of this code is validation if a user goes back up the list and chooses another value or selects the same value. /// <summary> /// Populates a change ddl based on the parent id of the previous ddl and adds the selection to a ChangeDetailDTO object. /// </summary> /// <param name="selectedValue"> This has to be a string because of the ability to edit the selected value </param> /// <param name="level"> </param> public async Task GetNextLevel ( string selectedValue, int level ) { //Get the appropriate Taxonomy List object var SelectedLevels=GetType().GetProperty(DDLGroup+ "Levels"?? "" ).GetValue( this, null ) as List<TaxonomyDdlDTO>; //if this is replacing a level that is last in the index, remove the old value. //further down I'm clearing a range if a new dd value is selected to remove all the child values if ( string.IsNullOrEmpty(selectedValue)) return; //if the selected value is not changed, do nothing. if (level <=SelectedLevels!.Count())
{ if (selectedValue==SelectedLevels[level -1 ].TaxonomyId) return;
} int selectedId=0; int.TryParse(selectedValue, out selectedId); //Parent int of 0 means its a top-level item if (selectedId !=0 )
{ var currentLevel=TaxonomyList.Where(x=> x.TaxonomyId==selectedValue).Single(); if (!SelectedLevels.Contains(currentLevel))
{
SelectedLevels.Add(currentLevel);
};
} else { if (SelectedLevels.Count <=level -1 && SelectedLevels[level - 2 ] !=null )
SelectedLevels.RemoveAt(level - 2 );

SelectedLevels.Add( new TaxonomyDdlDTO()
{
TaxonomyId=selectedValue,
Name=selectedValue
});
} //Event passes the new selection object to the parent page if (DDLGroup=="Current" ) await CurrentLevelSelectedEvent.InvokeAsync(SelectedLevels); else await NewLevelSelectedEvent.InvokeAsync(SelectedLevels); //populates the next dropdown list based on the selection justmade var nextLevelTaxonomy=TaxonomyList.Where(x=> x.ParentId==selectedId).ToList(); //Level5 has no children. if (level <=4 )
GetType().GetProperty( string.Concat( "L", level + 1 )).SetValue( this, nextLevelTaxonomy); if (SelectedLevels.Count> level)
SelectedLevels.RemoveRange(level -1, SelectedLevels.Count -1 );
} I appreciate any suggestions you have.

## Answer

**Chris** answered on 26 Oct 2023

I'm reading through my question again, and an answer hits me. Not sure if its the best answer but its simple. I just create a reference to each ddl and pass the properties I need to the method. The Id will be the Level (1-5) and Value is the value selected. So OnChange is now: OnChange="@(()=> GetNextLevelTest(DdlRef1.Value, DdlRef1.Id))" "Rubber Ducky" dev at it's finest!

### Response

**Chris** commented on 26 Oct 2023

I'm such a dork. Please disregard this question because I already have what I need. I wish I could just delete it...so embarrassing.

### Response

**Dimo** commented on 31 Oct 2023

Hi Chris, Getting component parameters from the component reference can work, but is not very "Blazor-ish". Better use the parameter variables: <TelerikComboBox Value="@L1Value " Id=" L1 " OnChange="@(()=> GetNextLevelTest( L1Value, " L1 "))" />
