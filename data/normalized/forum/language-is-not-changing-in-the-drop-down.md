# Language is not changing in the drop down

## Question

**Adn** asked on 03 Jul 2024

@using System.Threading @using Telerik.Blazor.Components @inject NavigationManager NavigationManager <div> <TelerikDropDownList Data="@Cultures" @bind-Value="@SelectedCulture" Width="200px" TextField="@nameof(CultureData.Text)" ValueField="@nameof(CultureData.Value)" DefaultText="Select a language"> <DropDownListSettings> <DropDownListPopupSettings Height="auto"></DropDownListPopupSettings> </DropDownListSettings> </TelerikDropDownList> </div> @code{ public class CultureData { public string Text { get; set; } public string Value { get; set; } } public List<CultureData> Cultures { get; set; }=new List<CultureData>() { new CultureData() { Text="English", Value="en-US" }, new CultureData() { Text="German", Value="de-CH" }, }; public string SelectedCulture { get; set; }=Thread.CurrentThread.CurrentUICulture.Name; protected override void OnInitialized() { if (Cultures.All(c=> c.Value !=SelectedCulture)) { SelectedCulture=Cultures.First().Value; } } public void OnValueChanged(string eventArgs) { SelectedCulture=eventArgs; SetCulture(eventArgs); } public void SetCulture(string culture) { var uri=new Uri(NavigationManager.Uri).GetComponents(UriComponents.PathAndQuery, UriFormat.Unescaped); var query=$"?culture={Uri.EscapeDataString(culture)}&redirectUri={Uri.EscapeDataString(uri)}"; NavigationManager.NavigateTo($"{NavigationManager.BaseUri}Culture/SetCulture{query}", forceLoad: true); } }

## Answer

**Nadezhda Tacheva** answered on 05 Jul 2024

Hello Adnan, The DropDownList configuration looks correct. I've tested the code but the language text is properly updated when I change the value from the DropDownList. I've extracted it in REPL: [https://blazorrepl.telerik.com/GouBkzPe23HzZKzF38.](https://blazorrepl.telerik.com/GouBkzPe23HzZKzF38.) The DropDownList declaration uses two-way value binding but I also noticed you've created a OnValueChanged method. I suspect on your end you may be using that, so you can set the culture when the user changes the DropDownList value. My best guess is that something is going wrong in the SetCulture, this blocks the page and the DropDownList value does not appear updated. To verify that, you may check the console for any errors and debug that part. Regards, Nadezhda Tacheva Progress Telerik
