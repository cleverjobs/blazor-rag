# pass a value from a page to Mainlayout or App.Blazor

## Question

**Moh** asked on 27 Oct 2024

hi I want to create a session after the user clicks on the button and display this user's information such as UserName or UserID in a section of the MainLayout In the MainLayout page, the currentUser_Id parameter value received from the session is displayed correctly in the paragraph, but this value is not passed to the paragraph inside the section. In fact, I want to show the value of User _id which is created in the login page and in the session in a part of the page app .razor or mainLayout .razor as user information. please help me LoginPage.razor: @page "/"
@using BlazorSessionApp.Layout
@layout LoginLayout
@inject NavigationManager NavigationManager
@inject ProtectedSessionStorage ProtectedSessionStore <button class="btn btn-primary" @onclick="Submit"> Enter </button> @code
{
private async Task Submit()
{
await ProtectedSessionStore.SetAsync("User_Id", 500);

NavigationManager.NavigateTo("/Home", true);
}
} App.razor : <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <base href="/" /> <link rel="stylesheet" href="bootstrap/bootstrap.min.css" /> <link rel="stylesheet" href="app.css" /> <link rel="stylesheet" href="BlazorSessionApp.styles.css" /> <link rel="icon" type="image/png" href="favicon.png" /> <HeadOutlet @rendermode="InteractiveServer" /> </head> <body> <SectionOutlet SectionName="mysection" /> <Routes @rendermode="InteractiveServer" /> <script src="_framework/blazor.web.js"> </script> </body> </html> MainLayou.razor : @inherits LayoutComponentBase
@inject ProtectedSessionStorage ProtectedSessionStore <p> OutOf Section:@currentUser_Id </p> <SectionContent SectionName="mysection"> <p> into My Section:@currentUser_Id </p> </SectionContent> <div class="page"> <div class="sidebar"> <NavMenu /> </div> <main> <div class="top-row px-4"> <a href="[https://learn.microsoft.com/aspnet/core/"](https://learn.microsoft.com/aspnet/core/") target="_blank"> About </a> </div> <article class="content px-4"> @Body </article> </main> </div> @code {
public int currentUser_Id;
public bool isConnected;

protected override async Task OnAfterRenderAsync(bool firstRender)
{
if (firstRender)
{
isConnected=true;
await LoadStateAsync();
StateHasChanged();
}
}
private async Task LoadStateAsync()
{
var result=await ProtectedSessionStore.GetAsync <int> ("User_Id");
currentUser_Id=result.Success ? result.Value : 0;
}
private async Task IncrementUser_Id()
{
currentUser_Id++;
await ProtectedSessionStore.SetAsync("User_Id", currentUser_Id);
}
}
