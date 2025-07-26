# InCell Editing with a checkbox

## Question

**MaxMax** asked on 30 Mar 2022

I have a checkbox in a grid (Telerik Grid for Blazor). When I click the checkbox (using incell editing) the value changes however it does not save to the database and if I leave the page and come back the data is back to the old values. This is the code for the grid: <TelerikGrid Class="custom-icons" Data="@OfficesList" Reorderable="true" EditMode="@GridEditMode.Incell" Sortable="true" Pageable="true" SelectionMode="GridSelectionMode.Multiple" OnUpdate="@UpdateItem" @ref="OfficeListGrid" @bind-SelectedItems="@SelectedItems"> <DetailTemplate Context="office"> <Incumbents Office="@office"> </Incumbents> </DetailTemplate> <GridColumns> <GridCommandColumn Context="OfficeCommandsContext"> <GridCommandButton Command="Edit" Class="btn btn-sm btn-primary" Icon="edit"> Edit </GridCommandButton> </GridCommandColumn> <GridColumn Field="@nameof(GetOfficesResult.OfficeName)" Title="Office" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.OfficeSeqNum)" Title="Office Sequence #" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.IsVacant)" Title="Is Vacant" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.IsPrimaryPartisan)" Title="Is Primary Partisan" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.IsPrimaryNonPartisan)" Title="Is Primary Non Partisan" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.PrimaryDistrictType)" Title="Primary Voting District Type" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.PrimaryDistrictCode)" Title="Primary Voting District" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.IsGeneral)" Title="Is General Ballot" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.GeneralDistrictType)" Title="General Voting District Type" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.GeneralDistrictCode)" Title="General Voting District" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.CanFileAgain)" Title="Can File Again?" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.TermLength)" Title="Term Length" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.FilingDistrictType)" Title="General Voting District Type" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.FilingDistrictCode)" Title="General Voting District" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.SalaryType)" Title="Salary Type" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.Salary)" Title="Salary" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.FilingFee)" Title="Filing Fee" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.NextElection)" Title="Next Election" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.Notes)" Title="Notes" Editable="false" /> <GridColumn Field="@nameof(GetOfficesResult.FederalOnly)" Title="Is Federal Only" /> </GridColumns> </TelerikGrid> This is the code behind for the Update Item: public async Task UpdateItem ( GridCommandEventArgs args ) { var currState=OfficeListGrid.GetState();

GetOfficesResult offices=(GetOfficesResult)args.Item; /// /Reset any current editing currState.EditField=null;
currState.OriginalEditItem=null; //Reset any current insertion currState.InsertedItem=null; //Add the item to edit to the state var target=OfficesList.FirstOrDefault(o=> o.OfficeID==offices.OfficeID); if (target !=null )
{
target.OfficeID=offices.OfficeID;
target.OfficeName=offices.OfficeName;
target.FilingDistrictCode=offices.FilingDistrictCode;
target.FilingDistrictType=offices.FilingDistrictType;
target.PrimaryDistrictCode=offices.PrimaryDistrictCode;
target.PrimaryDistrictType=offices.PrimaryDistrictType;
target.GeneralDistrictCode=offices.GeneralDistrictCode;
target.GeneralDistrictType=offices.GeneralDistrictType;
target.IsVacant=offices.IsVacant;
target.IsPrimaryPartisan=offices.IsPrimaryPartisan;
target.IsPrimaryNonPartisan=offices.IsPrimaryNonPartisan;
target.IsGeneral=offices.IsGeneral;
target.OfficeSeqNum=offices.OfficeSeqNum;
target.CanFileAgain=offices.CanFileAgain;
target.TermLength=offices.TermLength;
target.SalaryType=offices.SalaryType;
target.Salary=offices.Salary;
target.FilingFee=offices.FilingFee;
target.NextElection=offices.NextElection;
target.Notes=offices.Notes;
target.FederalOnly=offices.FederalOnly;
}

offices=args.Item as GetOfficesResult;

GetOfficesResult originalItem=OfficesList.Where(itm=> itm.OfficeID==offices.OfficeID).FirstOrDefault();
GetOfficesResult itemToEdit=GetOfficesResult.GetClonedInstance(originalItem); await OfficeListGrid.SetState(currState);
SelectedItems=OfficesList;

AddToSelectedCollection(itemToEdit); //Use the state to remove the edited item and close the editor //currState.EditField=null; //currState.OriginalEditItem=null; await OfficeListGrid.SetState(currState); await RebindGrid();
} I am not sure why it doesn't save Thank you in advance Max

## Answer

**Nadezhda Tacheva** answered on 04 Apr 2022

Hi Max, By default, the Grid will handle the update process for you. The event arguments of the OnUpdate event handler provide the updated item values. That said, you don't need to manually modify the state, the Grid will handle that out of the box. You just need to get the edited item from the Item field of the OnUpdate event arguments and cast it to your model. Then, call your service to update that item in the actual database. The OnUpdate handler code would look something like this: async Task UpdateHandler ( GridCommandEventArgs args ) {
GetOfficesResult item=(GetOfficesResult)args.Item; // perform actual data source operations here through your service await MyService.Update(item); // update the local view-model data with the service data await GetGridData();
} Generally speaking, it is indeed possible to initiate editing/inserting of an item through the Grid state. However, this approach will be more suitable if you want to somehow override the default behavior of the Grid editing. Otherwise, it is far easier to use the built-in editing functionalities the Grid provides. I am also adding a sample demonstrating using the default editing behavior, so you can see how much simpler it is compared to manually modifying the state to handle this operation. I'm sharing it via Telerik REPL for Blazor and you can directly run and test it in the browser - [https://blazorrepl.telerik.com/GwEeEykC45rGDcoE21.](https://blazorrepl.telerik.com/GwEeEykC45rGDcoE21.) In addition, I'd like to mention that the InCell edit mode is designed to deliver an Excel-like editing experience where one can click on a cell to start editing it. Having this in mind, you should not add an Edit command button as it contradicts with the InCell edit mode design. If you want to allow your users be able to initiate editing of an item via CommandButton click, you may consider the other edit modes the Grid supports - Inline and PopUp. I hope you will find the above information useful to move forward with your application. Please let us know if any further assistance is needed. Regards, Nadezhda Tacheva

### Response

**Max** commented on 04 Apr 2022

Thank you Nadezhda, This solution works partially. I can select the checkbox but the checkbox does not stay true (they are all defaulted to false) when I go to click on the next checkbox. Max

### Response

**Nadezhda Tacheva** commented on 07 Apr 2022

Hi Max, It sounds like the update process has not passed successfully. To be able to assist further, you may send us a runnable sample of your configuration. Thus, we can debug it on our end and see what might be missing. Thank you in advance! I will be looking forward to hearing from you!
