# Add new record dialog is not closing after add

## Question

**Mar** asked on 27 Jun 2024

In my grid I use pop-up edit. When I update a record the dialog closes, but not on add. Why? private async Task LoadUsers () { var users=await UserService.GetUsers();
Users=new ObservableCollection<User>(users);
} private async Task CreateHandler ( GridCommandEventArgs obj ) { if (obj.Item is not User user) return; var newUser=await UserService.Create(user); await LoadUsers();
} private async Task UpdateHandler ( GridCommandEventArgs args ) { if (args.Item is not User user) return; if (user.Id==0 ) return; var success=await UserService.Update(user);
} <TelerikGrid Data="@Users" height="100%" @bind-SelectedItems="@SelectedUsers" SelectionMode="GridSelectionMode.Single" EnableLoaderContainer="true" Sortable="true" Resizable="true" ConfirmDelete="true" ShowColumnMenu="true" OnUpdate="@UpdateHandler" OnCreate="@CreateHandler" OnStateInit="@((GridStateEventArgs<User> args)=> OnStateInitHandler(args))" EditMode="GridEditMode.Popup"> <GridToolBarTemplate> <GridSearchBox DebounceDelay="200" Class="width-60percent" /> <GridCommandButton Command="Add" Icon="@SvgIcon.Plus" ThemeColor="@ThemeConstants.Button.ThemeColor.Primary"> Add User </GridCommandButton> </GridToolBarTemplate> <GridSettings> <GridValidationSettings Enabled="true" /> <GridPopupEditSettings MinWidth="350px" /> </GridSettings> <GridColumns> <GridColumn Field="@nameof(User.Id)" Width="120px" Editable="false" /> <GridColumn Field="@nameof(User.Initials)" Width="135px" /> <GridColumn Field="@nameof(User.FirstName)" /> <GridColumn Field="@nameof(User.LastName)" /> <GridColumn Field="@nameof(User.WorkEmail)" Width="260px" /> <GridColumn Field="@nameof(User.ClientName)" Title="Client"> <EditorTemplate> @{ var u=(User)context; } <TelerikDropDownList ValueField="@nameof(CboItem.Id)" TextField="@nameof(CboItem.Name)" Filterable="true" FilterOperator="StringFilterOperator.Contains" Title="Select a client" DefaultText="Select a client" @bind-Value="@u.ClientId" Data="@TsClientCbos"> <DropDownListSettings> <DropDownListPopupSettings Height="500px" Width="350px" /> </DropDownListSettings> </TelerikDropDownList> </EditorTemplate> </GridColumn> <GridColumn Field="@nameof(User.Active)" Width="110px" ShowColumnMenu="true" /> <GridColumn Field="@nameof(User.IsBiEmployee)" Title="BI Employee" Width="120px" ShowColumnMenu="true" /> <GridColumn Field="@nameof(User.SyncToCloud)" Width="130px" ShowColumnMenu="true" Editable="false" /> <GridCommandColumn Width="110px"> <GridCommandButton Command="Save" Icon="@FontIcon.Save" Title="Update" ShowInEdit="true" /> <GridCommandButton Command="Cancel" Icon="@FontIcon.Cancel" ShowInEdit="true" /> <GridCommandButton Command="Edit" Icon="@FontIcon.Pencil" Title="Edit" Enabled="CanEdit" /> </GridCommandColumn> </GridColumns> </TelerikGrid>

### Response

**Hristian Stefanov** commented on 01 Jul 2024

Hi Martin, Thank you for sharing parts of your configuration. I have tried to recreate the described problem within our Grid Popup Editing demo. As a result, the popup seems to work correctly upon adding an item on my end. As a next step, could you send me a small runnable sample that reproduces the issue? That will allow me to investigate further the case. For your convenience, you can send me the code via the REPL platform. I look forward to hearing from you. Kind Regards, Hristian

### Response

**Martin Herløv** commented on 03 Jul 2024

I had and error that was blocking for the close action. Sorry for taking up your time

### Response

**Hristian Stefanov** commented on 03 Jul 2024

Hi Martin, Thank you for updating me on the situation. I'm glad to hear that you found the cause. Kind Regards, Hristian
