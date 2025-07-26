# TreeList: Show ConfirmDialog during OnCreate

## Question

**Tho** asked on 22 Oct 2024

Dear Community! I have the requirement to show a ConfirmDialog before actually saving objects to the database, because of some conditions that need to meet. Nevertheless my TreeList looks like follows and has the later OnCreate event defined: <TelerikTreeList Data="@Data" IdField="Server" ParentIdField="PreServer" Pageable="true" Height="100%" EditMode="@TreeListEditMode.Inline" OnCreate="@CreateServer" OnUpdate="@UpdateServer" OnDelete="@DeleteServer" OnEdit="@(()=> EditAction=!EditAction)" OnAdd="@(()=> AddAction=!AddAction)" ConfirmDelete="true"> </TelerikTreeList> My approach was simply to hook into the OnCreate event, place a Dialogs.ConfirmAsync and await the result before continuing. In fact, the confirm dialog shows up, but gets overlayed by a transparent container that has a higher z-index and prevents the confirm dialog to be clicked. Furthermore a loading spinner appears and the app gets stuck. I also tried to add a Task.Delay(1) but it didn't work out. async Task CreateServer ( TreeListCommandEventArgs args ) { await Task.Delay( 1 );

CancelCreate=await Dialogs.ConfirmAsync( "Please confirm.", "Confirmation" ); if (CancelCreate){
ServerViewModel server=(ServerViewModel)args.Item; if (server !=null )
{
server.PreServer=((ServerViewModel)args.ParentItem)?.Server; var result=await _sdService.CreateServer(server); if (result)
{
NotificationComponent?.Show( "Server created!", NotificationTheme.Success); await FetchData();
} else {
NotificationComponent?.Show( "An error occurred!", NotificationTheme.Error);
}
}
}
} Any help would be much appreciated. Many thanks!

## Answer

**Nadezhda Tacheva** answered on 24 Oct 2024

Hi Thomas, You may use the Class parameter of the TreeList to set a z-index style, which is lower than the default Dialog z-index of 10,000. For more details on creating a custom confirmation dialog, you may refer to this article: Customize the Delete Confirmation Dialog. It targets the Grid and the delete command, but the same approach can be used for a different command and the TreeList component. Regards, Nadezhda Tacheva Progress Telerik
