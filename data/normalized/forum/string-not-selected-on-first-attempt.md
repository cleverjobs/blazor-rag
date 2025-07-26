# string not selected on first attempt

## Question

**Ste** asked on 12 Apr 2021

Hello, I have an issue that I'd like to share with you. I have the following setup: Razor: @if (_isEditMode && _aListOfStrings.Any()) { <TelerikAutoComplete Data="_aListOfStrings" Filterable="true" FilterOperator="StringFilterOperator.Contains" @bind-Value="_aViewModel.aStringProperty"> </TelerikAutoComplete> } Code behind: protected override async Task OnParametersSetAsync() { await GetTheStringList(); } private async Task GetTheStringList () { _aListOfStrings=_aService.GetTheListOfStrings(); } The autocomplete renders like expected. The data is also shown and filtered like expected. For some reason, when I type a string that is present in "_aListOfStrings" and select it for the first time. The string is not filled-in the autocomplete, nor does it get bound to the model. The second time I filter and select the string, it does get filled in and bound to the model. Do you guys have any idea why this happens? I can't seem to figure it out. This is happening for all autocompletes in this "form". I've tried the following: 1. Render the Autocomplete outside of the Form 2. Set an id 3. Call this.StateHasChanged() after retrieving the data for the list 4. Changed OnParametersSetAsync() to OnInitilizedAsync() to fetch the list Thanks in advance!

## Answer

**Hristian Stefanov** answered on 14 Apr 2021

Hello Stefan, I tried to implement your code example for the AutoComplete filtering on the attached file and it worked just the way you want. Could you try using my code sample to compare it with your actual project and this way, you could see where something is missing? If you still have this problem, you could try to reproduce it on the attached project and send it back, so I can investigate? To attach an archive with a project you can open a support ticket in case the changes are bigger than a few lines of code. Regards, Hristian Stefanov

### Response

**Stefan** answered on 14 Apr 2021

Hello,Thank you for the reply. I found the cause by isolating everything; it seems to be the "k-card". When the autocomplete is wrapped like this: <div class="k-card" style="width: 480px;" <h5 class="card-header">The Title</h5> <div class="card-body"> ... The previously provided markup ... <div> </div> When the autocomplete is wrapped like this, the issue appears. Without the "k-card" the autocompletes seem to function like expected. Is this something that's fixable on your end? Or do you recommend me to use different css from the "k-card"?

### Response

**Hristian Stefanov** answered on 19 Apr 2021

Hello Stefan, I added the provided div part around my last example and it seems to work in the way you want. On the first line of the provided example, it is needed one more ">" at the end (but it might be just a typo). In the attached file, you will find the reworked example from the last time. As you said, by removing the "k-card" class, your autocomplete is working as expected, meaning your project might have css style sheet for "k-card", that is causing the issue. Check this just in case. I hope this helps and if you have any other questions, let me know. Regards, Hristian Stefanov Progress Telerik
