# TileLayout update HeaderText from TelerikCalendar need two StateHasChanged calls

## Question

**Pet** asked on 11 Jun 2021

Hi, in [https://docs.telerik.com/blazor-ui/knowledge-base/tilelayout-rendering-contents](https://docs.telerik.com/blazor-ui/knowledge-base/tilelayout-rendering-contents) is written, that StateHasChanged must called to Update the HeaderText. But with a TelerikCalendar in Content the HeaderText is one click to late: @page "/test" <TelerikTileLayout> <TileLayoutItems> <TileLayoutItem HeaderText="@date.ToShortDateString()"> <Content> <TelerikCalendar Value="@date" ValueChanged="@CalendarValueChangedHandler" /> </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> @code {

DateTime date { get; set; }=DateTime.Today;

public async void CalendarValueChangedHandler(DateTime newDate)
{
date=newDate;
StateHasChanged();
// await Task.Delay(50).ContinueWith(o=> { InvokeAsync(StateHasChanged); });
}

} I have to add a second call to StateHasChanged with a minimal Delay of 50 ms. It works with the line: await Task.Delay(50).ContinueWith(o=> { InvokeAsync(StateHasChanged); }); But this behavior is not normal? Regards, Peter

## Answer

**Nadezhda Tacheva** answered on 18 Jun 2021

Hi Peter, Stepping in to provide an update after further investigation on the case along with the development team. The key point in your scenario is that the ValueChanged handler of the Calendar is an async operation. For Blazor specific reasons when an async handler is used it is performed after the call of StateHasChanged, so the value used in rendering is the old one. Therefore, the second call of StateHasChanged after the delay delivers the desired result as the HeaderText update has already passed. The example in the mentioned knowledge base article is for a synchronous operation and thus comes the confusion. I will update it to also cover an async process use case. In the meantime, another approach you may try as a workaround that doesn't use delays is to use Templates - this will work since we're not assigning a new parameter to the component, but rather using the same template to get different values: <TelerikTileLayout>
<TileLayoutItems>
<TileLayoutItem>
<HeaderTemplate>
@date.ToShortDateString()
</HeaderTemplate>
<Content>
<TelerikCalendar Value="@date" ValueChanged="@CalendarValueChangedHandler"></TelerikCalendar>
</Content>
</TileLayoutItem>
</TileLayoutItems>
</TelerikTileLayout>

@code { public DateTime date { get; set; }=DateTime.Today; public async void CalendarValueChangedHandler ( DateTime newDate ) {
date=newDate; await InvokeAsync(StateHasChanged);
}
} I hope you will find the above information and example useful. If any further questions appear, please do not hesitate to contact us. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Eric R | Senior Technical Support Engineer** answered on 15 Jun 2021

Hi Peter, Thank you for providing the code sample. I was able to reproduce the same result. See the following workaround and sample. Workaround As a workaround, I recommend using the following async ValueChangedHandler. Note that it reduces the delay to 0 milliseconds and still works which should eliminate any delay if there was one. Sample Markup <TelerikTileLayout> <TileLayoutItems> <TileLayoutItem HeaderText="@SelectedDateString"> <Content> <TelerikCalendar Value="@date" ValueChanged="@CalendarValueChangedHandler" /> </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> Code Block DateTime date { get; set; }=DateTime.Today; string SelectedDateString { get; set; }=DateTime.Today.ToShortDateString(); public async Task CalendarValueChangedHandler ( DateTime newDate ) {
SelectedDateString=newDate.ToShortDateString();
date=newDate; await Task.Delay( 0 ).ContinueWith(o=> { InvokeAsync(StateHasChanged); });
} Wrapping Up Unfortunately, I don't believe dual async calls to be normal behavior and will need to follow up with the development team for further clarification. If it is discovered to be a bug I will create the proper tracking requests and follow up. In the meantime, please let me know if you need any additional information. Thank you for using the UI for Blazor forums. Regards, Eric R | Senior Technical Support Engineer

### Response

**Peter** answered on 17 Jun 2021

Hi Eric, Thank you. So only one call is necessary with no delay. I found an other problem: How can I force the Caledar to show the correct month, if I change the date by code? Markup <TelerikTileLayout> <TileLayoutItems> <TileLayoutItem HeaderText="@SelectedDateString"> <Content> <TelerikCalendar Value="@date" ValueChanged="@CalendarValueChangedHandler" /> </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> <TelerikButton OnClick="SetDate"> Set Tomorrow </TelerikButton> Code Block DateTime date { get; set; }=DateTime.Today; string SelectedDateString { get; set; }=DateTime.Today.ToShortDateString(); public async Task CalendarValueChangedHandler ( DateTime newDate ) {
SelectedDateString=newDate.ToShortDateString();
date=newDate; await Task.Delay( 0 ).ContinueWith(o=> { InvokeAsync(StateHasChanged); });
} public async Task SetDate ( ) {
date=DateTime.Today.AddDays( 1 );
SelectedDateString=date.ToShortDateString(); await Task.Delay( 0 ).ContinueWith(o=> { InvokeAsync(StateHasChanged); });
} Select a date from a different month an then set the date to tomorrow with the Button. All is fine, but the calendar month page is not set to the month of tomorrow. Best regards, Peter

### Response

**Eric R | Senior Technical Support Engineer** commented on 17 Jun 2021

As a best practice, we like to keep our thread topics separated. As a result, I have created and responded to a new ticket for you that can be found in your Telerik Account at 1524432.

### Response

**Peter** commented on 18 Jun 2021

Thank you for your solution, which set also the Date parameter: <TelerikCalendar Date="@date" Value="@date" ValueChanged="@CalendarValueChangedHandler" />

### Response

**Peter** answered on 18 Jun 2021

Hi Nadezhda, the template solution is fine. Then a simple call of StateHasChanged() is ok, because the ChangedHandler is called from the main thread. To get the same format I add <HeaderTemplate> <h5 class="k-card-title"> @date.ToShortDateString() </h5> </HeaderTemplate> which is used from the parameter HeaderText. Regards, Peter
