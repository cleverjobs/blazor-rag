# Add row button on Grid causes edit form submit?

## Question

**TomTom** asked on 04 May 2019

I've got a TelerikGrid inside a Blazor EditForm component (abridged code): <EditForm Model="@_billOfLadingVM" OnValidSubmit="@HandleValidSubmit"> other bound components here <TelerikGrid Data=@_billOfLadingVM.BillOfLadingContainers EditMode="incell" Pageable="true"> <TelerikGridEvents> <EventsManager OnUpdate="@UpdateHandler"></EventsManager> </TelerikGridEvents> <TelerikGridToolBar> <TelerikGridCommandButton Command="Create" Icon="add">Add Container</TelerikGridCommandButton> </TelerikGridToolBar> <TelerikGridColumns> @*<TelerikGridColumn Field=@nameof(HSCodeModel.HSCodeId) Title="ID" Editable="false" />*@<TelerikGridColumn Field=@nameof(BillOfLadingContainerModel.ContainerCode) Title="Container Code" /> <TelerikGridColumn Field=@nameof(BillOfLadingContainerModel.ContainerSizeId) Title="Container Size" /> <TelerikGridColumn Field=@nameof(BillOfLadingContainerModel.IsLCL) Title="LCL" /> <TelerikGridCommandColumn> <TelerikGridCommandButton Command="Update" Icon="save" ShowInEdit="true">Update</TelerikGridCommandButton> <TelerikGridCommandButton Command="Edit" Icon="edit">Edit</TelerikGridCommandButton> <TelerikGridCommandButton Command="Delete" Icon="delete">Delete</TelerikGridCommandButton> <TelerikGridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</TelerikGridCommandButton> </TelerikGridCommandColumn> </TelerikGridColumns> </TelerikGrid> </EditForm> When I press the Create command button (i.e. add new row in grid) in the grid's toolbar it seems like it causes the form to be submitted as the OnValidSubmit method is called. Is that the expected behaviour and is there any way to stop that happening? My grid is updating child data of my `_billOfLadingVM` model class, so I don't want the grid to submit the whole form as the user may still have other data to enter in the other components. The obvious solution is to move the grid outside of edit form component tags, but that's tricky to do with this particular form's layout.

## Answer

**Marin Bratanov** answered on 06 May 2019

Hi Tom, The standard button clicks fire the submit event in a standard scenario, for example, we can modify the FetchData page from the default template like this and you will see how both events fire (information continues after the snippet): @page "/fetchdata" @using BlazorServerApp.Data @inject WeatherForecastService ForecastService <h1>Weather forecast</h1> <p>This component demonstrates fetching data from a service.</p> @if (forecasts==null ) { <p><em>Loading...</em></p> } else { <EditForm Model="@person" OnValidSubmit="@HandleValidSubmit"> <DataAnnotationsValidator /> <ValidationSummary /> <InputText id="name" bind-Value="@person.Name" /> <table class="table"> <thead> <tr> <th>Date</th> <th>Temp. (C)</th> <th>Temp. (F)</th> <th>Summary</th> </tr> </thead> <tbody> @foreach (var forecast in forecasts) { <tr> <td><button onclick="@TestClick">click me</button></td> <td>@forecast.Date.ToShortDateString()</td> <td>@forecast.TemperatureC</td> <td>@forecast.TemperatureF</td> <td>@forecast.Summary</td> </tr> } </tbody> </table> </EditForm> } @functions { Person person=new Person() { Name="John Smith" }; void TestClick() { Console.WriteLine( "clicked at " + DateTime.Now); } void HandleValidSubmit() { Console.WriteLine( "OnValidSubmit" ); } public class Person { public string Name { get; set; } } WeatherForecast[] forecasts; protected override async Task OnInitAsync() { forecasts=await ForecastService.GetForecastAsync(DateTime.Now); } } This makes me think that this is how validation is expected to work in Blazor, at least at the moment (who knows, maybe more features or properties will come up in the future that will let us control this). What I can suggest you consider at the moment is to use a flag in the OnClick event of the grid toolbar buttons and check that flag in the OnValidSubmit handler. Perhaps a timestamp can be useful to see how much time passed since the grid button click - if it is too little, obviously the validation was triggered by a button in the grid, and you can prevent further logic from running. Perhaps for other buttons you could go towards using a <button type="button"> because the type defaults to submit and will submit the form. If you would like to see something similar for our buttons, you could post a public feature request in our

### Response

**Tom** answered on 07 May 2019

Hi Marin That's really interesting, thanks for the info. I think I'm probably misunderstanding the current validation model in Blazor - I'll do some reading on that. However, at the moment the default behaviour is that if you have a Telerik Blazor grid inside a form you cannot add a row to that grid if something else on the form is invalid. For example, if I have a text input bound to a field that requires data I cannot add a row to the grid, because when the grid's Create button is pressed the form fails validation, focus moves to the first invalid control and the grid row add never completes. I'm not sure that's the right behaviour for the grid in that situation? I think the form validation model is normally that you can keep entering bad data, but the form shows you what's failing validation? If we had a scenario where it was either "enter data into the grid or enter some data in this text area" the default behaviour of the grid would prevent that at present (because you can't add a row to the grid). It seems to me that the grid should trigger validation after the row add is complete rather than when the add button is pressed?

### Response

**Marin Bratanov** answered on 07 May 2019

Hi Tom, We need to first wait for the Blazor events to become more manageable, so one can control their propagation: [https://github.com/aspnet/AspNetCore/issues/5545.](https://github.com/aspnet/AspNetCore/issues/5545.) Having that would let us stop the propagation and so the form validation would not be triggered. Ideally, I also think that the grid should allow you to add a row regardless of the rest of the page, but at the moment either event control must be implemented in the framework, or the Telerik button needs to be able to render different button types. Ultimately, perhaps both. We have this on our radar, and we will be monitoring the framework development so we can act upon it. Regards, Marin Bratanov

### Response

**Tom** answered on 07 May 2019

Thanks Marin, that's useful to know. In the short term would any of these solutions be possible as a quick temporary change to the grid behaviour while Microsoft sort out the plan for the events - it seems like that may take a while to get resolved: When rendering a toolbar button with `Command="Create"` change it to render as a `type=button`? Or perhaps make that behaviour one of the options for the grid so as not to break existing code? Change the grid to have an option where all the buttons are rendered as `type=button` and then we can wire them up manually ourselves using the existing grid events? Or is there any way to add a method to the grid (or use an existing method) to allow a row to be added without calling the submit, that we could then wire up to a separate button's `onclickevent` outside the grid that we could then set to `type=button'?

### Response

**Marin Bratanov** answered on 08 May 2019

Hello Tom, We have been discussing this and we have decided to make the grid buttons render as <button type="button"> so they don't raise validation and form submission. In fact, I will get on that right after i click "send" on this message. We are aiming at pushing a release next week with a few fixes (like nullable types improvements), so I hope this one will make it in it too. Regards, Marin Bratanov

### Response

**Tom** answered on 08 May 2019

That's great news Marin, many thanks

### Response

**Marin Bratanov** answered on 09 May 2019

You're welcome, Tom. Thank _you_ for pointing this out. This should be out with our next release, barring some critical/regression issue QA finds. --Marin
