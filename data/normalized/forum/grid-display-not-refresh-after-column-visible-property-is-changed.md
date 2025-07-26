# Grid display not refresh after column Visible property is changed

## Question

**Rém** asked on 02 Mar 2022

Hi, I'm using a TelerikGrid to display some results and I'd like to let the user select the results he wants to keep on screen by having a button "Edit" that makes a checkboxColumn visible in order to select/deselect the items he wants to keep. Problem is : This is my button declaration :<GridCommandButton Command="EditDisplayedResults" OnClick="OpenEditMode" IconClass="fa fa-edit"></GridCommandButton> And this is its handler protected async Task OpenEditMode() { editMode=true; Console.WriteLine("Open Edit mode"); StateHasChanged(); } Now when I click on the button the event is well triggered but the column doesn't appear directly after the Visible property is set to true. Even with the StateHasChanged is doesn't rerender the grid. The only way to make the column appear is by changing page. Is there a ay to rerender the grid in my case ? And if possible without having to reload the data because it takes some time... Thanks in advance Rémy
