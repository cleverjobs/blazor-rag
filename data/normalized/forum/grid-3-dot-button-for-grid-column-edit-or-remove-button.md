# Grid 3 dot button for grid column edit or remove button

## Question

**Sun** asked on 29 Dec 2023

For mobile view in column item i want to add the a three dot menu. On click of that button there will be a popup with two buttons (Like image) I tried a number of things but not able to figure out which component will be helpful in this condition. Any help will be appreciated (Kendo Blazor)

## Answer

**Nansi** answered on 03 Jan 2024

Hi Sunil, When the user clicks on the three dots, you can use a Context Menu to show the Edit and Remove items. Here is a code example and bullet points for achieving the result: 1. Add a TelerikButton in a GridCommandColumn <GridCommandColumn> <TelerikButton Icon="@SvgIcon.MoreVertical" OnClick="@( (MouseEventArgs args)=> MyCustomOnClickHandler(args, (SampleData)context) )"> </TelerikButton> </GridCommandColumn> 2. Show the Context Menu programmatically with the received coordinates of the button click event: private async Task MyCustomOnClickHandler ( MouseEventArgs args, SampleData dataItem ) {
SelectedPerson=dataItem; await ContextMenuRef.ShowAsync(args.ClientX, args.ClientY);
} 3. Also programmatically enter Grid edit mode through the Grid State: case "Edit": var currState=GridRef.GetState(); currState.InsertedItem=null;
SampleData itemToEdit=SampleData.GetClonedInstance(GridData.Where(itm=> itm.ID==SelectedPerson.ID).FirstOrDefault()); currState.OriginalEditItem=itemToEdit; await GridRef.SetStateAsync(currState); break; 4. Handle the removal of the Grid row in the same way as in a desktop view but with manually created GridCommandEventArgs: case "Remove": var deleteArgs=new GridCommandEventArgs(); deleteArgs.Item=SelectedPerson; OnGridDelete(deleteArgs); break; private void OnGridDelete ( GridCommandEventArgs args ) {
SampleData item=(SampleData)args.Item;
GridData.Remove(item);
} Let me know if you need something more. On a side note, please ask the license holder at your company to assign you a license, so that your account is in good standing. Alternatively, activate a trial to show that you are evaluating our product. Regards, Nansi Progress Telerik
