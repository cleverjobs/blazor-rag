# Using the Telerik Menu to go back to the Home page in Blazor

## Question

**Mik** asked on 28 May 2025

Hello Everyone, I'm working on a Blazor Server project, and I've replaced the default navigation menu with a TelerikMenu component. It produces this: When I click the Counter, Weather, etc, I get to the correct page. Here's how my project is layed out: You can see that the Home.razor page is in the same location as the Weather and Counter page. I'm also able to get to the pages under the DisplayData folder. Here's the code: <div> <img src="picture.png" style="height: 300px; margin-right: 10px;"> </div> <TelerikMenu Data="@MenuData" Orientation=@MenuOrientation.Vertical> </TelerikMenu> @code{ public List<MenuItem> MenuData { get; set; } public class MenuItem { public string Text { get; set; } public string Url { get; set; } public ISvgIcon Icon { get; set; } public List<MenuItem> Items { get; set; }
} protected override void OnInitialized () {
GenerateMenuData();
} public void GenerateMenuData () {
MenuData=new List<MenuItem>()
{ new MenuItem()
{
Text="Home",
Url="Home",
Icon=SvgIcon.Home
}, new MenuItem()
{
Text="Counter",
Url="Counter",
Icon=SvgIcon.Calculator
}, new MenuItem()
{
Text="Weather",
Url="Weather",
Icon=SvgIcon.Globe
}, new MenuItem()
{
Text="Display Data",
Url="",
Icon=SvgIcon.Data,
Items=new List<MenuItem>()
{ new MenuItem()
{
Text="Delme Table",
Url="/DelMeTable",
Icon=SvgIcon.Data // SvgIcon.User }, new MenuItem()
{
Text="Delme Telerik",
Url="/DelmeTelerikTable",
Icon=SvgIcon.Data
}, new MenuItem()
{
Text="Delme Telerik SQL",
Url="/DelmeTelerikTableSQL",
Icon=SvgIcon.Data
}
}
}
}; //end of MenuData } //end of GenerateMenuData() // } When I try to get back to the Home page, I get a "Not Found" error. Also of note, when the application launches to the Home page, here is the URL (from the debugger): localhost:7044. My question is, how do I set the URL for the home page to get back to it? Thanks, Mike

## Answer

**Justin** answered on 30 May 2025

Hi Michael, Thank you for the question and the detailed information. By default, when a Blazor project is created with the Visual Studio template, the routing attribute of the Home.razor page is set to @page "/", which navigates to the base URL. For example [https://localhost:xxxx.](https://localhost:xxxx.) Where as the rest of the Razor pages will normally follow the pattern of @page "/NameOfRazorPage". To Navigate to the Home.razor page, change the Url field of the MenuItem that represents the Home page to Url="/". Regards, Justin Progress Telerik

### Response

**Mike** commented on 30 May 2025

Hi Justin, Thank you very much for the explanation as well as telling me how to set the Url value for the home page. It worked perfectly!! Best regards, Mike
