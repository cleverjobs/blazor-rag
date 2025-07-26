# Is this a bug?

## Question

**EdEd** asked on 08 Feb 2021

Hi, I am having the wierdest problem. I have a treelist with 2 editable fields. One is templated with a textbox, the other with a textarea. I can type into the textbox with no problem. But when I type in the textarea, the first letter goes in, but after that, it somehow puts the focus back to the first textbox. I can only type on char at a time into the text area. Any ideas? Thanks ... Ed <TelerikTreeList Data="@CommentsData" ItemsField="@(nameof(CommentItem.Children))" @ref="CommenterTL" Pageable="true" Sortable="true" FilterMode="@TreeListFilterMode.FilterMenu" SelectionMode="@TreeListSelectionMode.Multiple" Resizable="true" Reorderable="true" EditMode="@TreeListEditMode.Inline" OnCreate="@CreateComment" OnUpdate="@UpdateComment" OnDelete="@DeleteComment"> @*OnUpdate="@UpdateItem"*@<TreeListToolBar> <TreeListCommandButton Command="Add" Icon="add">Add</TreeListCommandButton> </TreeListToolBar> <TreeListColumns> <TreeListColumn Title="Subject" Width="250px" Field="FindComment.Subject" Editable="true" Expandable="true"> <EditorTemplate Context="ctx"> @{ var item=(ctx as CommentItem); if (item.FindComment==null) item.FindComment=new FindComment(); <TelerikTextBox @bind-Value="@item.FindComment.Subject"> </TelerikTextBox> } </EditorTemplate> </TreeListColumn> <TreeListColumn Title="Comment" Resizable="false" Editable="true" Field="FindComment.Comment" Width="350px"> <EditorTemplate Context="ctx1"> @{ var c=(ctx1 as CommentItem); if (c.FindComment==null) c.FindComment=new FindComment(); <TelerikTextArea @bind-Value="@c.FindComment.Comment" Width="325px" Class="TelerikTextAreaWidth"> </TelerikTextArea> } </EditorTemplate> </TreeListColumn> <TreeListColumn Title="Name" Width="250px" Field="CommenterName" Editable="false"> </TreeListColumn> <TreeListCommandColumn Width="150px"> @{ if (SelectedComment !=null && SelectedComment.FindComment.Id==appData.AppUser.Id || appData.AppUser.RoleId==(int)ROLE_ENUM.SysAdmin) { <TreeListCommandButton Command="Add" Icon="add"></TreeListCommandButton> <TreeListCommandButton Command="Edit" Icon="edit"></TreeListCommandButton> <TreeListCommandButton Command="Delete" Icon="delete"></TreeListCommandButton> <TreeListCommandButton Command="Save" Icon="save" ShowInEdit="true"></TreeListCommandButton> <TreeListCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"></TreeListCommandButton> } else { <TreeListCommandButton Command="Add" Icon="add"></TreeListCommandButton> <TreeListCommandButton Command="Save" Icon="save" ShowInEdit="true"></TreeListCommandButton> <TreeListCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"></TreeListCommandButton> } } </TreeListCommandColumn> </TreeListColumns> </TelerikTreeList>

## Answer

**Marin Bratanov** answered on 08 Feb 2021

Hi Ed, Does this happen only in Insert mode? We are aware of such an issue (you can Follow it here, I've added your Vote), but I am unable to reproduce a problem in edit mode. I am attaching here a video and a test page so you can see if I am missing something. Regards, Marin Bratanov

### Response

**Ed** answered on 08 Feb 2021

Yes, you are correct, it only happens in insert mode. Any ideas for a work around?

### Response

**Marin Bratanov** answered on 08 Feb 2021

I'm afraid I don't have a workaround for this issue with the InLine editing, Ed. Perhaps the best idea I can offer is trying the popup edit mode of the treelist. Regards, Marin Bratanov

### Response

**Ed** answered on 12 Feb 2021

It's happening in teh pop mode too. :-(

### Response

**Marin Bratanov** answered on 13 Feb 2021

Hello Ed It seems to work fine for me, and I am attaching here a video from some of my tests. Am I missing something? Regards, Marin Bratanov
