# Add new item and focus

## Question

**Ran** asked on 17 Oct 2019

Hi, When I hit the add button on a grid, I notice that the focus does not go to the first cell of the newly added row for editing. This is kind of annoying. How can I force this? Thanks ... Ed <TelerikGrid Data=@GridData Pageable="true" Groupable="true" Sortable="true" OnUpdate="@UpdateHandler" OnCreate="@CreateHandler" OnEdit="@EditHandler"> <GridColumns> <GridColumn Field="Name" /> <GridColumn Field="IsActive" Title="Is Active"> </GridColumn> <GridCommandColumn Width="300px"> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton> <GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton> </GridCommandColumn> </GridColumns> <GridToolBar> <GridCommandButton Command="Add" Icon="add">Create Role</GridCommandButton> </GridToolBar> </TelerikGrid>

## Answer

**Marin Bratanov** answered on 17 Oct 2019

Hi Ed, At the moment, there is no provision for this. Perhaps you could use the OnClick event of the Add Command Button to invoke a JS interop call that will find and .focus() the first input it finds on the grid, but this can become difficult if you have more grids rendered. There is already a feature request for defining a default focus in the grid and I suggest you Follow it to get status updates (I have added your Vote for your): [https://feedback.telerik.com/blazor/1408647-specifying-which-field-should-have-focus-in-grid-editor.](https://feedback.telerik.com/blazor/1408647-specifying-which-field-should-have-focus-in-grid-editor.) If you have suggestions on how this should be exposed for configuration, I encourage you to post them there. Regards, Marin Bratanov

### Response

**Randy Hompesch** answered on 17 Oct 2019

Ok, thanks. Good to know it's in the pipeline.
