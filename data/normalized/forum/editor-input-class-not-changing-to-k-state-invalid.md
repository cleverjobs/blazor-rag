# Editor input class not changing to k-state-invalid

## Question

**BobBob** asked on 01 Oct 2020

I have an editor which is in a component that is used in several different pages. The validation on the Editor seems to be working as when I try to submit my form, it does give me the validation summary saying the editor content is required, however when I view the html markup in dev tools, the class on the input still says 'k-state-valid'. I need to it to be k-state-invalid as I want to change the border color to red when it is invalid. I have placed a simple editor on one of the pages and when I do that it seems to work just fine, so I think it has something to do with it being in a component. Below is the form that contains the component and the component itself. Any help would be appreciated. <EditForm Model="@newTicket" OnValidSubmit="@CreateTicket"> <div id="NewTicket" class="container-fluid"> <ValidationSummary /> <DataAnnotationsValidator /> <TicketHeader Ticket="@newTicket"></TicketHeader> <div class="form-group row"> <div class="col"> <TelerikTextBox Class="defaultFocus" Id="subject" @bind-Value="@newTicket.Subject" Label="Subject"></TelerikTextBox> </div> </div> <div class="form-group row"> <div class="col"> <AttachmentsUploader Attachments="@newTicket.Attachments"></AttachmentsUploader> </div> </div> <div class="form-group row editor"> <div class="col"> <label for="Details" class="ticketLabel">Ticket Details</label><br /> <PostEditor @bind-Content="@newTicket.Detail" IsPublic="true" ShowPublicTool="false" EditorHeight="90%"></PostEditor> </div> </div> <div class="form-group row"> <div class="col"> <TelerikButton ButtonType="ButtonType.Submit" Primary="true" Enabled="@(!loaderVisible)" Class="float-right ml-2"> <PleaseWait Type="PleaseWaitType.Button" Visible="@loaderVisible" ThemeColor="@ThemeColors.Light" /> @(loaderVisible ? "Saving" : "Save") </TelerikButton> <TelerikButton ButtonType="ButtonType.Button" @onclick="CancelButtonClick" Enabled="@(!loaderVisible)" Class="float-right"> Cancel </TelerikButton> </div> </div> </div> </EditForm> PostEditor.razor @using Telerik.Blazor.Components.Editor @inject IJSRuntime jSRuntime <TelerikEditor @ref="editor" Id="Comment" Value="@Content" ValueChanged="ContentChanged" ValueExpression="@( ()=> Content )" Tools="@tools" Width="100%" Height="@EditorHeight"> <EditorCustomTools> <EditorCustomTool Name="Public"> <label class="k-label mr-1">Public</label> <TelerikSwitch Value="@IsPublic" ValueChanged="IsPublicChanged" ValueExpression="@( ()=> IsPublic )" OnLabel="Yes" OffLabel="No"></TelerikSwitch> </EditorCustomTool> <EditorCustomTool Name="ColorTools"> <TelerikButtonGroup> <ButtonGroupButton OnClick="ShowFontColor" Title="Font Color"> <i class="fas fa-font" style="color: @fontColor"></i> </ButtonGroupButton> <ButtonGroupButton OnClick="ShowBackColor" Title="Text Highlight Color"> <i class="fas fa-highlighter"></i> </ButtonGroupButton> <ButtonGroupButton OnClick="ExecuteCleanFormatting" Icon="@IconName.ClearCss" Title="Clean Formatting"> </ButtonGroupButton> </TelerikButtonGroup> <input type="color" id="fontColor" name="fontColor" @bind="@FontColorSelected" /> <input type="color" id="backColor" name="backColor" @bind="@BackColorSelected" /> </EditorCustomTool> </EditorCustomTools> </TelerikEditor> @code { [Parameter] public string Content { get; set; } [Parameter] public EventCallback<string> ContentChanged { get; set; } [Parameter] public bool IsPublic { get; set; } [Parameter] public EventCallback<bool> IsPublicChanged { get; set; } [Parameter] public bool ShowPublicTool { get; set; } [Parameter] public string EditorHeight { get; set; } private string fontColor="#000000"; private string FontColorSelected { get { return fontColor; } set { var changeEventArgs=new ChangeEventArgs(); changeEventArgs.Value=value; Task.Run(()=> ExecuteForeColor(changeEventArgs)); } } private string backColor="#FFFFFF"; private string BackColorSelected { get { return backColor; } set { var changeEventArgs=new ChangeEventArgs(); changeEventArgs.Value=value; Task.Run(()=> ExecuteBackColor(changeEventArgs)); } } private TelerikEditor editor; private List<IEditorTool> tools=new List<IEditorTool> { new EditorButtonGroup(new Bold(), new Italic(), new Underline()), new EditorButtonGroup(new AlignLeft(), new AlignCenter(), new AlignRight()), new CustomTool("ColorTools"), new UnorderedList(), new InsertTable(), new EditorButtonGroup(new AddRowBefore(), new AddRowAfter(), new MergeCells(), new SplitCell()), new Format(), new FontSize(), new FontFamily() }; protected override void OnInitialized() { if (ShowPublicTool) { tools.Add(new CustomTool("Public")); } base.OnInitialized(); } private async Task ExecuteBackColor(ChangeEventArgs e) { backColor=e.Value.ToString(); await editor.ExecuteAsync(new FormatCommandArgs("backColor", backColor)); } private async Task ExecuteCleanFormatting() { await editor.ExecuteAsync(new ToolCommandArgs("cleanFormatting")); fontColor="#000000"; backColor="#ffffff"; } private async Task ExecuteForeColor(ChangeEventArgs e) { fontColor=e.Value.ToString(); await editor.ExecuteAsync(new FormatCommandArgs("foreColor", fontColor)); } private async Task ShowBackColor() { await jSRuntime.InvokeVoidAsync("showBackColor"); } private async Task ShowFontColor() { await jSRuntime.InvokeVoidAsync("showFontColor"); } }

## Answer

**Svetoslav Dimitrov** answered on 06 Oct 2020

Hello Bob, So far, the Editor does not support the k-state-invalid CSS class. You can make your own CSS class that makes the border-color of the editor red and apply it when the validation does not pass using the Class parameter of the component. In order to do so, I have used the EditContext to check if there are any validation messages for the property bound to the Editor and used the OnValidationStateChanged event to call StateHasChanged to render anew the component so that the CSS rules that come from the Class are applied. I have created a sample, which shows how this could be achieved: @*This is the custom class that mimics k-state-invalid*@<style>.myCustomInvalidState { border-color: #dc3545;
} </style> @using System.ComponentModel.DataAnnotations <EditForm EditContext="@MyEditContext" OnValidSubmit="@HandleValidSubmit"> <DataAnnotationsValidator /> <ValidationSummary /> <TelerikEditor @bind-Value="@theProduct.Description" Class="@(IsEditorInvalidSubmit ? " myCustomInvalidState ": "")"> </TelerikEditor> <TelerikButton ButtonType="@ButtonType.Submit"> Submit </TelerikButton> </EditForm> @code {
protected EditContext MyEditContext { get; set; }

public FieldIdentifier EditorFieldIdentifier { get; set; } // instantiating a FieldIdentifier for the Editor,
// see the OnInitialize on how to pass the model and the field

//checking for validation messages for the editor
public bool IsEditorInvalidSubmit=> MyEditContext.GetValidationMessages(EditorFieldIdentifier).Any();

//calling StateHasChanged to render the component again
private void HandleValidationStateChanged(object o, ValidationStateChangedEventArgs args)=> StateHasChanged();

protected override void OnInitialized()
{
MyEditContext=new EditContext(theProduct);
EditorFieldIdentifier=new FieldIdentifier(theProduct, nameof(theProduct.Description));
MyEditContext.OnValidationStateChanged +=HandleValidationStateChanged;
}

public class Product
{
[Required(ErrorMessage="Description is required")]
[MaxLength(100, ErrorMessage="The max allowed length of the content is 100 symbols")]
[MinLength(20, ErrorMessage="The min allowed length of the content is 20 symbols")]
public string Description { get; set; }
}

Product theProduct=new Product();

void HandleValidSubmit()
{
}
} Regards, Svetoslav Dimitrov

### Response

**Bob** answered on 06 Oct 2020

Perfect! Thanks.
