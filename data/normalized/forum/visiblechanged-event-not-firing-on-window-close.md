# visiblechanged event not firing on window close

## Question

**Law** asked on 12 May 2021

The VisibleChangedHandler is never hit, either on open or close. Using version 2.23.0 My code/markup is as such: <TelerikWindow Visible="@documentWindowVisible" VisibleChanged="@VisibleChangedHandler"> <WindowTitle>View/Manage Attachment</WindowTitle> <WindowContent> <div id="tooltipmanagedocument" title="View Current Document"></div> <TelerikEditor @bind-Value="@currentAttachment.Content"></TelerikEditor> <TelerikButton OnClick="@UpsertDocument" Icon="save"></TelerikButton> <TelerikButton OnClick="@ExportToPDF" Icon="download"></TelerikButton> <label> Upload Attachment (will overwrite existing Attachment but retain history) <InputFile OnChange="@LoadDocumentFromDisk" accept=".docx"/> </label> </WindowContent> <WindowActions> <WindowAction Name="Maximize"></WindowAction> <WindowAction OnClick="hideManageDocument" Name="Close"></WindowAction> </WindowActions> </TelerikWindow> public void VisibleChangedHandler(bool currVisible) { if (currVisible) { documentWindowVisible=true; if (IsThereACurrentAttachment) { LoadDocumentFromDB(); } else { // need to make load document button invisible } } else { documentWindowVisible=false; } }

### Response

**Lawrence** commented on 12 May 2021

I may have found it but it doesn't explain everything. I am also using "WindowAction" for the close event and that OnClick event is firing ok and perhaps taking the visibility change event? However, even if that is happening it doesn't explain why the visibility change event doesn't fire when it becomes visible.

## Answer

**Marin Bratanov** answered on 12 May 2021

Hello Lawrence, The VisibleChanged event fires only when the user closes the window from the built-in close command. Changing the Visible field in the view-model will hide that window without raising the event - changing values in the view-model never raises events because that can cause an endless loop. If you are changing the value with your own code, you can call the next code you want to run with your own code as needed, instead of relying on component events. So, the following seems to work fine for me, and I am attaching a short video of the expected behavior as a reference so you can confirm if I am missing something: @result

<TelerikButton OnClick="@ToggleWindow">Toggle the Window</TelerikButton>

<TelerikWindow Visible="@isVisible" VisibleChanged="@VisibleChangedHandler">
<WindowTitle>
<strong>The Title</strong>
</WindowTitle>
<WindowContent>
This is my window <strong>popup</strong> content.
</WindowContent>
<WindowActions>
<WindowAction Name="Close" />
</WindowActions>
</TelerikWindow>

@code { bool isVisible { get; set; } string result { get; set; } void VisibleChangedHandler ( bool currVisible ) // this will always come in as false {
isVisible=currVisible; // if you don't do this, the window won't close because of the user action result=$"the window is now visible: {isVisible} ";

Console.WriteLine( "The user closed the window with the [x] button on its toolbar" );
} public void ToggleWindow ( ) {
isVisible=!isVisible;

result=$"the window is now visible: {isVisible} ";
}
} If this does not help you move forward, please edit your post to show a fully runnable version of my snippet that does not fire the event when expected so I can have a look. Regards, Marin Bratanov

### Response

**Suresh Krishna** commented on 09 Feb 2022

Hi Marin Bratanov, I have almost a similar issue. I have my Togglewindow function from another component(parent). <PopModal CallBackTabstrip="CallRefreshHistoryInTabstripFromModalPopup" @bind-WindowIsVisible="@Visible" @ref="popmodalref" Title="@selfilename" IsFolder="IsFolder"></PopModal> protected async Task ToggleWindow(string file_name) { fileName=file_name; string imgpath="\\wwwroot\\Resources\\"; string filewoext=System.IO.Path.GetFileNameWithoutExtension(file_name); if (Directory.Exists($"{Directory.GetCurrentDirectory()}{imgpath + filewoext }")) { selfilename=System.IO.Path.GetFileNameWithoutExtension(file_name); Visible=true; IsFolder=true; //popmodalref.Refresh(); } else { IsFolder=false; if (Visible) { Visible=!Visible; } // Visible=!Visible; await Task.Run(ReadFile); await OnImageClicked.InvokeAsync(_ImageIndex); //Visible=false; // popmodalref.Refresh(); } } Telerikwindow component <TelerikWindow Width="600px" Height="600px" Visible="@WindowIsVisible" VisibleChanged="@VisibleChangedHandler" Modal="true"> <WindowTitle> <strong>@Title</strong> </WindowTitle> <WindowContent> @*<Lighting rowCount="3" FolderPath="@Title"></Lighting>*@<Buttonarray OnImageClicked="CallRefreshHistoryInButtonArray" rowCount="3" FolderPath="@Title"></Buttonarray> @*<div style="padding-left:35%;"> <button style="padding:20px;" @onclick="CloseWindow">Close the Window</button> </div>*@</WindowContent> <WindowActions> <WindowAction Name="Close"></WindowAction> </WindowActions> </TelerikWindow> void VisibleChangedHandler(bool currVisible) { WindowIsVisible=currVisible; } Its like a infinite loop now as once I trigger the window. what ever action i do the window pops up.!!

### Response

**Suresh Krishna** commented on 10 Feb 2022

Hey, I have fixed it by moving the window to the same window instead of a separate component. Thanks,

### Response

**Marin Bratanov** commented on 10 Feb 2022

I think the issue is that the parent component didn't get its parameter updated - for @bind- to work, the child component must raise a <ParameterName>Changed event (in this case this should be done in the VisibleChangedHandler) that will update the parameter in the parent component (the Visible parameter in this case). Otherwise, the next time the component re-renders, the Visible parameter with value true will be given to the child component and it will obey it (and in this case the window will show).
