# Combobox without value and now doesn't render

## Question

**JohJoh** asked on 17 Feb 2022

Hi, I started a small blazor project some week ago. I've stared the project before the release 3.0 (I use the trial).But since then, I've updated to 3.0.1 The main component I use is the Grid and the combobox. I have a sketch of my project to make a demo on the computer of my customer. On my machine (AMD Rzyen 5800H, Win 11, VS2022) eveything runs file. The first component is just a combobox that displays a list of date. The I tried to deploy on the demo server of my customer (Win server 2019, IIS) and when I launch the app, the combobox is empy... but the code is just a list of date to display After spending several hours, I've decided to create an "empty" blazor project in order to test the combobox and deploy on the server and now, it's worse, enve on my computer, this new project is not able to display the combobox I used the simpliest sample from the documentation, still the same. Does anyone noticed something similar? is it a licence problem? why my elder developpement works fine and not the newest? @page "/counter" <PageTitle> Counter </PageTitle> <h1> Counter </h1> <p role="status"> Current count: @currentCount </p> <button class="btn btn-primary" @onclick="IncrementCount"> Click me </button> <TelerikButton OnClick="@OnClickHandler"> Hello! </TelerikButton> <TelerikComboBox Data="@MyList" @bind-Value="MyItem"> </TelerikComboBox> @code {
private int currentCount=0;
string result;

private void IncrementCount()
{
currentCount++;
}

protected List <string> MyList=new List <string> () { "first", "second", "third" };

protected string MyItem { get; set; }

//Define a preselected value when the component initializes
protected override void OnInitialized()
{
MyItem="second";
}
async Task OnClickHandler()
{
result=DateTime.Now.ToString();
}
} (PS on my new project, i followed all the instructions [https://docs.telerik.com/blazor-ui/getting-started/server-blazor](https://docs.telerik.com/blazor-ui/getting-started/server-blazor) ) Regards;

### Response

**Marin Bratanov** commented on 17 Feb 2022

Looks like the Telerik Theme is not loaded at all, check the browser console for 404 errors for assets, and for any other errors. Perhaps when deployed the base URL is different so you will need to tweak it with an <environment> tag in the host page?
