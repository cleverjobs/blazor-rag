# How to Use Window and EditContext Together?

## Question

**Por** asked on 20 Nov 2019

I would like to be able to use the Telerik window component within my forms... for example, a field where you select a person from a database - but finding that person is a complicated search - so instead of a dropdown, it's a display only field that has an ellipsis button next to it, and it would open a window, where they would find a person, select the person, and then pass back the selection to the main form. But the telerik blazor window doesn't seem to render within the scope of the form that you nest it under, so the containing EditContext is not available, and I have tried everything I can think of to get the data back from the window and update the main form data behind the scenes, but the EditContext still doesn't know about the change. Example Below (3 files) FormTest.razor: @page "/formtest/" @using SMS5.BApp.Classes <CascadingValue Value="@MyStuff"> <div class="sms-tab-content"> <EditForm EditContext="@StuffForm" @key="@(" FormEditCtx1")"> <div>MAIN FORM:</div> <div> SomeStuff1: <InputText @bind-Value="@MyStuff.SomeStuff1"></InputText> SomeStuff2: <InputText @bind-Value="@MyStuff.SomeStuff2"></InputText> </div> <div>Component Containing Window:</div> <WindowTest2 OnChanged="@StuffGotUpdated"></WindowTest2> </EditForm> <div> <div>Log of changes to form context:</div> <textarea @bind="@Log" cols="150" rows="20"></textarea> </div> </div> </CascadingValue> @code { protected EditContext StuffForm { get; set; } public Stuff MyStuff=new Stuff() { SomeStuff1="foo", SomeStuff2="bar"}; public string Log { get; set; } protected override void OnInitialized() { StuffForm=new EditContext(MyStuff); StuffForm.OnFieldChanged +=EditContext_OnFieldChanged; } private void EditContext_OnFieldChanged(object sender, FieldChangedEventArgs e) { // code to save goes here var x=e.FieldIdentifier.FieldName; Log +="--" + x +" changed.--"; StateHasChanged(); } protected void StuffGotUpdated() { StateHasChanged(); } } WindowTest2.razor: @using SMS5.BApp.Classes <div> <div> <TelerikButton OnClick="@OpenWin"> Open Window </TelerikButton> </div> <div> <div>In window component, outside of window, from cascading parameter:</div> Some Stuff 1:<InputText @bind-Value="@MyStuff.SomeStuff1"></InputText> Some Stuff 2:<InputText @bind-Value="@MyStuff.SomeStuff2"></InputText> </div> </div> <TelerikWindow Top="50px" Left="100px" Visible="@IsVisible"> <WindowTitle> <strong>The Title</strong> </WindowTitle> <WindowActions> <WindowAction Name="Minimize" /> <WindowAction Name="Maximize" /> <WindowAction Name="Close" /> </WindowActions> <WindowContent> <div> <input @bind-value="@SomeStuff1Local" /> (local var copied to and back from SomeStuff1) </div> <div> <input @bind-value="@MyStuff.SomeStuff2" /> (direct bind to MyStuff.SomeStuff2) </div> <TelerikButton OnClick="@CloseWin"> Close Window </TelerikButton> </WindowContent> </TelerikWindow> <TelerikButton OnClick="@InvokeCallback"> Refresh All </TelerikButton> @code { [CascadingParameter] public Stuff MyStuff { get; set; } [Parameter] public EventCallback<string> OnChanged { get; set; } public bool IsVisible { get; set; }=false; public string SomeStuff1Local { get; set; } protected void OpenWin() { IsVisible=true; SomeStuff1Local=MyStuff.SomeStuff1; StateHasChanged(); } protected void CloseWin() { IsVisible=false; MyStuff.SomeStuff1=SomeStuff1Local; StateHasChanged(); } protected void InvokeCallback() { OnChanged.InvokeAsync("blah"); } protected override void OnInitialized() { } } Stuff.cs: namespace SMS5.BApp.Classes { public class Stuff { public string SomeStuff1 { get; set; } public string SomeStuff2 { get; set; } } } p.s. I am still working of a reproducible example for the grid inline editing with EF proxy issue, it is going to take a little while to get that together. Thanks Portia

## Answer

**Marin Bratanov** answered on 21 Nov 2019

Hi Portia, Indeed, the Window renders at the root, as explained at the end of this article: [https://docs.telerik.com/blazor-ui/components/window/position.](https://docs.telerik.com/blazor-ui/components/window/position.) This is necessary for proper positioning. At the end of this post I am attaching a simple sample that showcases how this scenario works. I also made a KB article here: [https://docs.telerik.com/blazor-ui/knowledge-base/window-does-not-update-parent.](https://docs.telerik.com/blazor-ui/knowledge-base/window-does-not-update-parent.) On using the model (edit context) from the parent component - you should be able to create an edit context from the model coming in through the cascading value and then invoke an event that will update the parent component (this is important, as the UI won't otherwise update). Below is how I changed the window component and it seems to pass the values on clicking Close (I highlighted the changes). The EditForm I added is just in case you want to add validation there as well, otherwise merely invoking the event will suffice, because it will trigger the UI update - the new values are already in the model, but the UI has not changed and you see the old data - calling StateHasChanged() on the main form component resolves that. In fact, since the OnChange event is an EventCallback, it will automatically call StateHasChanged() so you can remove that protected void StuffGotUpdated ( ) { // StateHasChanged(); } @using SMS5.BApp.Classes

<div>
<div>
<TelerikButton OnClick="@OpenWin">
Open Window
</TelerikButton>
</div>
<div>
<div>In window component, outside of window, from cascading parameter:</div>
Some Stuff 1:<InputText @bind-Value="@MyStuff.SomeStuff1"></InputText>
Some Stuff 2:<InputText @bind-Value="@MyStuff.SomeStuff2"></InputText>
</div>
</div>

<TelerikWindow Top="50px" Left="100px" Visible="@IsVisible">
<WindowTitle>
<strong>The Title</strong>
</WindowTitle>
<WindowActions>
<WindowAction Name="Minimize" />
<WindowAction Name="Maximize" />
<WindowAction Name="Close" />
</WindowActions>
<WindowContent> <EditForm EditContext="@TheEditContext"> <div>
<input @bind- value="@SomeStuff1Local" /> (local var copied to and back from SomeStuff1)
</div>
<div>
<input @bind- value="@MyStuff.SomeStuff2" /> (direct bind to MyStuff.SomeStuff2)
</div>
<TelerikButton OnClick="@CloseWin">
Close Window
</TelerikButton> </EditForm> </WindowContent>
</TelerikWindow>

<TelerikButton OnClick="@InvokeCallback">
Refresh All
</TelerikButton>

@code {

[ CascadingParameter ] public Stuff MyStuff { get; set; }

[ Parameter ] public EventCallback<string> OnChanged { get; set; } protected EditContext TheEditContext { get; set; } public bool IsVisible { get; set; }=false; public string SomeStuff1Local { get; set; } protected void OpenWin ( ) {
IsVisible=true;
SomeStuff1Local=MyStuff.SomeStuff1;
StateHasChanged();
} protected void CloseWin ( ) {
IsVisible=false;
MyStuff.SomeStuff1=SomeStuff1Local; InvokeCallback(); StateHasChanged();
} protected void InvokeCallback ( ) {
OnChanged.InvokeAsync( "blah" );
} protected override void OnInitialized ( ) {
TheEditContext=new EditContext(MyStuff);
} } Regards, Marin Bratanov

### Response

**Portia** answered on 21 Nov 2019

Hello, Thanks for the reply. I think my example was overly complicated and did not illustrate the issue very well. Attached is a new one-page example that shows the issue more clearly. The model and/or values of the parent get updated - that is not the problem; the problem is that the EditContext does not know the model has changed, so IsModified() is not correct, and application does not know there is data to be saved. EditContext has an option for MarkAsUnmodifed(), but I haven't been able to find anything that works in the reverse direction. @page "/formtest/" <CascadingValue Value="@MyStuff"> <div class="sms-tab-content"> <EditForm EditContext="@StuffForm" @key="@(" FormEditCtx1")"> <div class="row"> <div class="col-sm-3"> <TelerikButton OnClick="@SaveData" Enabled="@SaveEnabled" Primary="true"> Save </TelerikButton> </div> <div class="col-sm-9"> <div>EditContext Info:</div> <div> Modified: @StuffForm.IsModified().ToString() </div> </div> </div> <div style="padding:20px;"> <div>MAIN FORM:</div> <div> SomeStuff1: <InputText @bind-Value="@MyStuff.SomeStuff1" @ref="@refOuterStuff1"></InputText> SomeStuff2: <InputText @bind-Value="@MyStuff.SomeStuff2"></InputText> </div> </div> <div style="padding:20px;"> <div> <TelerikButton OnClick="@OpenWin"> Open Window </TelerikButton> </div> </div> <TelerikWindow Top="50px" Left="100px" Visible="@IsVisible"> <WindowTitle> <strong>The Title</strong> </WindowTitle> <WindowActions> <WindowAction Name="Minimize" /> <WindowAction Name="Maximize" /> <WindowAction Name="Close" /> </WindowActions> <WindowContent> <div> <input @bind-value="@SomeStuff1Local" /> (local var copied to and back from SomeStuff1) </div> <div> <input @bind-value="@MyStuff.SomeStuff2" /> (direct bind to MyStuff.SomeStuff2) </div> <TelerikButton OnClick="@CloseWin"> Close Window </TelerikButton> </WindowContent> </TelerikWindow> </EditForm> <div> <div>Log of changes to form context:</div> <textarea @bind="@Log" cols="100" rows="10"></textarea> </div> </div> </CascadingValue> @code { public class Stuff { public string SomeStuff1 { get; set; } public string SomeStuff2 { get; set; } } public InputText refOuterStuff1 { get; set; } protected EditContext StuffForm { get; set; } public Stuff MyStuff=new Stuff() { SomeStuff1="foo", SomeStuff2="bar" }; public string Log { get; set; } bool SaveEnabled { get; set; }=false; protected override void OnInitialized() { StuffForm=new EditContext(MyStuff); StuffForm.OnFieldChanged +=EditContext_OnFieldChanged; } private void EditContext_OnFieldChanged(object sender, FieldChangedEventArgs e) { // code to save goes here var x=e.FieldIdentifier.FieldName; Log +=x + " changed." + "\n"; SaveEnabled=true; StateHasChanged(); } public bool IsVisible { get; set; }=false; public string SomeStuff1Local { get; set; } protected void OpenWin() { IsVisible=true; SomeStuff1Local=MyStuff.SomeStuff1; StateHasChanged(); } protected void CloseWin() { IsVisible=false; MyStuff.SomeStuff1=SomeStuff1Local; StateHasChanged(); } protected void SaveData() { //blah } }

### Response

**Portia** answered on 21 Nov 2019

Just figured out I can do this, which is working for me now: protected void CloseWin() { IsVisible=false; MyStuff.SomeStuff1=SomeStuff1Local; var fieldid=StuffForm.Field("Stuff.SomeStuff1"); StuffForm.NotifyFieldChanged(fieldid); StateHasChanged(); } I do think it would be a very helpful feature to have the option for a window that renders where you put it in the dom tree. In kendo/jquery world it never really mattered, but with Blazor it is going to be a lot of extra code to pull stuff in and out of the window.

### Response

**Marin Bratanov** answered on 22 Nov 2019

Hi Portia, Notifying the context for changes is a correct approach for such a case - this is how you can communicate changes from one component to another. I am not aware of a better solution and I would have liked an overload to NotifyFieldCHanged that indicates all fields or that the framework should check, as the current API requires that you pass a precise field (although it works fine whichever one you pass, and if you don't care what exactly the user changed any argument will do). I created a KB article about this as well: [https://docs.telerik.com/blazor-ui/knowledge-base/window-in-form-edit-context.](https://docs.telerik.com/blazor-ui/knowledge-base/window-in-form-edit-context.) That said, I have raised the question with the dev team so we can see if some other workaround will be possible about rendering in-place, as that would let it be part of the current form - which would also let validation work. I have one in mind, but it feels a bit hack-ish to me, so I wanted to run it by the component dev for feedback first. I will write back here once I have more information. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 25 Nov 2019

Indeed, there is a hack that will let the window render in the place of declaration, but we don't support such a scenario and I can't say whether it may lead to issues. Depending on the component and HTML element hierarchy, you may not see any problems, or you may have wrong positions or even a window that's never visible, because its parent has special positioning or overflow: hidden, for example. Thus, I am providing this just as an option you could try, but we can't say if it will actually be usable in a real scenario. This will, by the way, also let you use <InputText> and validation summary/message components inside the window as part of the parent form so you can also use validation and notify the user of issues with their input, in addition to the ability to share the same context. That said, here follows the hack. Note that his is another TelerikRootComponent element that you add around the window so it renders at its place of declaration. The TelerikRootComponent at the root of the <app> should stay there and it is the place where our popups should render. <TelerikRootComponent> <TelerikWindow Top="50px" Left="100px" Visible="@IsVisible">. . . . </TelerikWindow> </TelerikRootComponent> Regards, Marin Bratanov
