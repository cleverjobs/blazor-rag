# Disable Left Mouse Click on Editor Template in Telerik Editit: Incell Mode

## Question

**ACV** asked on 07 Mar 2023

Hi, I have a question. I had a grid which EditMode is Incell and a column had "Editor Template". In this column - "Email", I tried to edit a cell by clicking both left and right mouse, and both of it worked at same way. I used Grid State to edit cell by right mouse clicking. The problem is: I want to disable edit mode by left click, the cell will edit if it was clicked by right mouse only. Many thanks. <TelerikGrid Data="@ListUser" ColumnVirtualization="true" Width="100%" Height="inherit" Sortable="true" Resizable="true" OnCancel="@Rebind" OnDelete="@DeleteItem" EditMode="@GridEditMode.Incell" OnEdit="@EditColumnView" OnUpdate="@UpdateHandler" FilterMode="@GridFilterMode.FilterRow" @ref="@GridRef"> <GridColumns> <GridColumn Field="@(nameof(VwModiFyUser.Email))" Editable="@edit_Permission" Title="Email" Width="21%"> <Template> @{ VwModiFyUser item=context as VwModiFyUser; <div @oncontextmenu:preventDefault="true" @oncontextmenu="@(()=>{CurrentUser_Name=context as VwModiFyUserEdit_Email2(CurrentUser_Name.RoleuserId);})"> @((context as VwModiFyUser).Email) </div> } </Template> <EditorTemplate> @{ VwModiFyUser item=context as VwModiFyUser; <TelerikTextBox @bind-Value="item.Email" OnChange="@(()=>Edit_Email(item.RoleuserId))" OnBlur="@CloseEditorAndSave" Width="100%" /> } </EditorTemplate> private async Task Edit_Email(int RoleUserID) { var currState=GridRef.GetState(); VwModiFyUser originalItem=List_User.Where(i=> i.RoleuserId==RoleIDUserID).FirstOrDefault(); VwModiFyUser itemToEdit=originalItem; currState.EditField="Email"; currState.EditItem=itemToEdit; currState.OriginalEditItem=originalItem; await GridRef.SetStateAsync(currState); }

## Answer

**Dimo** answered on 09 Mar 2023

Hello Tai, Use @onclick:stopPropagation for the <div> inside the column template. Also, remove the default cell paddings and move them to the <div>, so that users can't click outside the <div>. Regards, Dimo Progress Telerik

### Response

**ACV IT** commented on 09 Mar 2023

Thank you very much. It worked
